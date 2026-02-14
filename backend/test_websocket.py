import socketio
import time

# Crear cliente SocketIO
sio = socketio.Client()

@sio.event
def connect():
    print("Conectado al servidor!")

@sio.event
def connect_error(data):
    print("La conexión falló!")

@sio.event
def disconnect():
    print("Desconectado del servidor!")

@sio.on('mensaje_servidor')
def on_message(data):
    print('Mensaje recibido:', data)

@sio.on('nuevas_noticias')
def on_news(data):
    print('Noticias recibidas:', data)

def main():
    try:
        sio.connect('http://localhost:5000')
        sio.wait()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
