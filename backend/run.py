# Programa Principal

from app.ConectorAPI import ConectorAPI
from app.NoticiaFactory import NoticiaFactory
from app.Clasificador import clasificar_noticia
# vamos hacer una interfaz grafica

def main():
    ure_google_news = 'https://news.google.com/news/rss'
    conector = ConectorAPI(ure_google_news)
    news = conector.get_google_news()
    Noticias = NoticiaFactory.create_noticia(news)
    for Noticias in Noticias:
        print(f"Título: {Noticias.titulo}")
        print(f"Medio de comunicacion:{Noticias.medio}")
        print(f"Enlace: {Noticias.link}")
        print(f"Fecha: {Noticias.data_publicacion}")
        sesgo = clasificar_noticia(Noticias.medio,Noticias.titulo)
        print(f"Clasificación: {sesgo}")
        print("---")
    # Crear un objeto Noticia y agregarlo a la lista de noticias
    


    # Vamos a clasificar las noticias con nuestra Metodo Clasificador

if __name__ == '__main__':
    main()



