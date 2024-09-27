# Programa Principal
# Vamos a obtener las ultimas noticias desde Google News con Beautiful Soap.
# Primero, debemos importar las librerias necesarias.
import bs4
import re
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

# Abrimos la URL de Google News
# conecxion
ure_google_news = 'https://news.google.com/news/rss'
cliente = urlopen(ure_google_news)
contenido_xml = cliente.read()
cliente.close()

#lectura en el formato XML
pagina = soup(contenido_xml, 'xml')
items = pagina.find_all('item')

# Iterar cada noticia o cada item
for item in items:
    print('Titulos:', item.title.text)
    print('Enlace:', item.link.text)
    print('Fecha publicacion:', item.pubDate.text)

    print('=' * 70)





