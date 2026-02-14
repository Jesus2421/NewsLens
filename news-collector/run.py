# Programa Principal

from app.ConectorAPI import ConectorAPI
from app.NoticiaFactory import NoticiaFactory
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/noticias', methods=['GET'])
def get_noticias():
    url_google_news = 'https://news.google.com/news/rss'
    conector = ConectorAPI(url_google_news)
    news = conector.get_google_news()
    Noticias = NoticiaFactory.create_noticia(news)
    resultado = []
    for noticia in Noticias:
        resultado.append({
            'titulo': noticia.titulo,
            'medio': noticia.medio,
            'link': noticia.link,
            'fecha': noticia.data_publicacion
        })
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)