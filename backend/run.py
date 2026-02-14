# Programa Principal

from flask import Flask, send_from_directory, request
from flask_socketio import SocketIO, emit
from app.ConectorAPI import ConectorAPI
from app.NoticiaFactory import NoticiaFactory
from app.Clasificador import clasificar_noticia
import time
import threading
import os
import datetime

# Configurar rutas para servir el frontend
FRONTEND_FOLDER = os.path.abspath("../Frontend/InterfazGreficaWEB")
app = Flask(__name__, static_folder=FRONTEND_FOLDER, static_url_path='')
app.config['SECRET_KEY'] = 'secret!'

# Configuración CORS permisiva para desarrollo
socketio = SocketIO(app, cors_allowed_origins="*", logger=True, engineio_logger=True)

# Variable global para almacenar las últimas noticias
ULTIMAS_NOTICIAS = []

def fetch_and_emit_news():
    """Función en segundo plano para obtener y emitir noticias periódicamente"""
    global ULTIMAS_NOTICIAS
    ure_google_news = 'https://news.google.com/rss?hl=es-419&gl=AR&ceid=AR:es-419' 
    conector = ConectorAPI(ure_google_news)
    
    # Intervalo de actualización: 24 horas (86400 segundos)
    UPDATE_INTERVAL = 86400 
    
    while True:
        print("\n--- INICIANDO CICLO DE BÚSQUEDA DE NOTICIAS ---")
        try:
            news = conector.get_google_news()
            print(f"DEBUG: Conector devolvió {len(news)} items.")
            
            noticias_procesadas = []
            
            if news:
                try:
                    lista_noticias = NoticiaFactory.create_noticia(news)
                except Exception as e_factory:
                    print(f"ERROR CRÍTICO en NoticiaFactory: {e_factory}")
                    lista_noticias = []

                for noticia in lista_noticias:
                    try:
                        medio_safe = noticia.medio if noticia.medio else "Google News"
                        titulo_safe = noticia.titulo if noticia.titulo else "Sin título"
                        sesgo = clasificar_noticia(medio_safe, titulo_safe)
                        
                        noticia_data = {
                            'titulo': titulo_safe,
                            'medio': medio_safe,
                            'link': noticia.link,
                            'fecha': noticia.data_publicacion,
                            'clasificacion': sesgo
                        }
                        noticias_procesadas.append(noticia_data)
                    except Exception:
                        continue
                
                if noticias_procesadas:
                    ULTIMAS_NOTICIAS = noticias_procesadas # Guardar en caché
                    print(f"✅ EMITIENDO {len(noticias_procesadas)} NOTICIAS AL FRONTEND.")
                    socketio.emit('nuevas_noticias', {'noticias': noticias_procesadas})
                else:
                    print("⚠️ Alerta: Lista procesada vacía.")
            else:
                print("⚠️ Alerta: Lista vacía del conector.")
                
        except Exception as e:
            print(f"❌ ERROR GENERAL EN HILO DE NOTICIAS: {e}")
        
        # Calcular próxima actualización
        next_run = datetime.datetime.now() + datetime.timedelta(seconds=UPDATE_INTERVAL)
        print(f"--- FIN DEL CICLO. Próxima actualización: {next_run.strftime('%Y-%m-%d %H:%M:%S')} ---\n")
        
        time.sleep(UPDATE_INTERVAL)

@socketio.on('connect')
def handle_connect():
    print(f'✅ CLIENTE CONECTADO: {request.sid}')
    emit('mensaje_servidor', {'data': 'Conexión exitosa con Hamilton Backend'})
    
    # Enviar inmediatamente las noticias en caché si existen
    if ULTIMAS_NOTICIAS:
        print(f"📤 Enviando {len(ULTIMAS_NOTICIAS)} noticias en caché al nuevo cliente.")
        emit('nuevas_noticias', {'noticias': ULTIMAS_NOTICIAS})
    else:
        print("⚠️ No hay noticias en caché para enviar aún.")

@socketio.on('solicitar_noticias_manual')
def handle_manual_request():
    print(f'🔄 Cliente {request.sid} solicitó noticias manualmente.')
    if ULTIMAS_NOTICIAS:
        emit('nuevas_noticias', {'noticias': ULTIMAS_NOTICIAS})

@app.route('/')
def index():
    if app.static_folder:
        return send_from_directory(app.static_folder, 'index.html')
    return "Error: Carpeta estática no configurada"

@app.route('/<path:path>')
def serve_static(path):
    if app.static_folder:
        return send_from_directory(app.static_folder, path)
    return "Error: Carpeta estática no configurada"

def main():
    news_thread = threading.Thread(target=fetch_and_emit_news)
    news_thread.daemon = True
    news_thread.start()
    
    print(f"Iniciando servidor en puerto 5000...")
    socketio.run(app, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)

if __name__ == '__main__':
    main()
