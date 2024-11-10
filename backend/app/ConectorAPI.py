import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
class ConectorAPI():
    def __init__(self, url):
        self.url = url
    def get_google_news(self):
        url = self.url
        cliente = urlopen(url)
        contenido_xml = cliente.read()
        cliente.close()
        pagina = soup(contenido_xml, 'xml')
        items = pagina.find_all('item')
        noticias = []
        for item in items:
            noticia = {
                'title': item.title.text,
                'link': item.link.text,
                'description': item.description.text,
                'pubDate': item.pubDate.text
            }
            noticias.append(noticia)
        return noticias
