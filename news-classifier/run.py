from flask import Flask, request, jsonify
from app.classifier import clasificar_noticia

app = Flask(__name__)

@app.route('/clasificar', methods=['POST'])
def clasificar():
    data = request.get_json()
    medio = data.get('medio', '')
    titulo = data.get('titulo', '')
    if not medio or not titulo:
        return jsonify({'error': 'Faltan datos: medio y titulo son requeridos'}), 400
    sesgo = clasificar_noticia(medio, titulo)
    return jsonify({'sesgo': sesgo})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
