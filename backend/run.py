# Programa Principal
from app import utils

def main():
    noticias = utils.get_google_news()
    for noticia in noticias:
        print('Titulos:', noticia['title'])
        print('Enlace:', noticia['link'])
        print('Fecha publicacion:', noticia['pubDate'])
        print('=' * 70)

if __name__ == '__main__':
    main()







