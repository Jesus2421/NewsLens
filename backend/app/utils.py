import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

def get_google_news():
    ure_google_news = 'https://news.google.com/news/rss'
    cliente = urlopen(ure_google_news)
    contenido_xml = cliente.read()
    cliente.close()

    pagina = soup(contenido_xml, 'xml')
    items = pagina.find_all('item')

    noticias = []
    for item in items:
        noticia = {
            'title': item.title.text,
            'link': item.link.text,
            'pubDate': item.pubDate.text
        }
        noticias.append(noticia)

    return noticias

