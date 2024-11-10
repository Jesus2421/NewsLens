# Programa Principal

from app.ConectorAPI import ConectorAPI
from app.NoticiaFactory import NoticiaFactory
# vamos hacer una interfaz grafica

def main():
    ure_google_news = 'https://news.google.com/news/rss'
    conector = ConectorAPI(ure_google_news)
    news = conector.get_google_news()
    # Crear un objeto Noticia y agregarlo a la lista
    Noticias = NoticiaFactory.create_noticia(news)
    for Noticias in Noticias:
        print(f"Título: {Noticias.titulo}")
        print(f"Medio de comunicacion:{Noticias.medio}")
        print(f"Enlace: {Noticias.link}")
        print(f"Descripción: {Noticias.descripcion}")
        print(f"Fecha: {Noticias.data_publicacion}")
        print("---")

if __name__ == '__main__':
    main()



