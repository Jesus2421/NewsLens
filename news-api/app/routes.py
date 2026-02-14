import requests
from flask import Blueprint, jsonify

bp = Blueprint('api', __name__)

NEWS_COLLECTOR_URL = 'http://localhost:5001/noticias'
NEWS_CLASSIFIER_URL = 'http://localhost:5002/clasificar'

@bp.route('/noticias', methods=['GET'])
def get_noticias():
    # Obtener noticias del microservicio collector
    resp = requests.get(NEWS_COLLECTOR_URL)
    if resp.status_code != 200:
        return jsonify({'error': 'No se pudo obtener noticias'}), 500
    noticias = resp.json()
    # Clasificar cada noticia usando el microservicio classifier
    noticias_clasificadas = []
    for noticia in noticias:
        medio = noticia.get('medio', '')
        titulo = noticia.get('titulo', '')
        clas_resp = requests.post(NEWS_CLASSIFIER_URL, json={'medio': medio, 'titulo': titulo})
        if clas_resp.status_code == 200:
            sesgo = clas_resp.json().get('sesgo', 'desconocido')
        else:
            sesgo = 'desconocido'
        noticia['sesgo'] = sesgo
        noticias_clasificadas.append(noticia)
    return jsonify(noticias_clasificadas)
