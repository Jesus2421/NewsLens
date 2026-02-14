def clasificar_sesgo(medio):
    # Normalizar entrada
    if not medio:
        return "desconocido"
    
    medio_norm = medio.lower().strip()
    
    # Diccionario normalizado (claves en minúsculas)
    media_sesgos = {
        # Medios Internacionales
        "the wall street journal": "derecha",
        "abc7 los angeles": "centro",
        "the hill": "derecha",
        "ign": "centro",
        "the globe and mail": "izquierda",
        "deadline": "centro",
        "good news network": "centro",
        "reuters": "centro",
        "reuters.com": "centro",
        "engadget": "centro",
        "haaretz": "izquierda",
        "the associated press": "centro",
        "ap": "centro",
        "abc news": "centro",
        "politico": "centro",
        "politico europe": "centro",
        "shore daily news": "derecha",
        "new york post": "derecha",
        "scitechdaily": "centro",
        "the new york times": "izquierda",
        "nytimes": "izquierda",
        "the washington post": "izquierda",
        "fox news": "derecha",
        "axios": "centro",
        "forbes": "derecha",
        "cnn": "izquierda",
        "bbc": "centro",
        "bbc.com": "centro",
        "the verge": "centro",
        "al jazeera": "izquierda",
        "the guardian": "izquierda",
        
        # Medios en Español (Comunes en Google News AR/ES)
        "infobae": "derecha",
        "clarín": "derecha",
        "clarin": "derecha",
        "la nación": "centro",
        "la nacion": "centro",
        "página 12": "izquierda",
        "pagina 12": "izquierda",
        "el destape": "izquierda",
        "c5n": "izquierda",
        "tn": "izquierda",
        "todo noticias": "centro",
        "perfil": "izquierda",
        "ámbito": "izquierda",
        "ambito": "izquierda",
        "cronista": "centro",
        "el país": "izquierda",
        "el pais": "izquierda",
        "el mundo": "centro",
        "abc": "derecha",
        "la vanguardia": "derecha",
        "rt": "izquierda",
        "telesur": "izquierda",
        "infobae américa": "derecha"
    }
    
    # Verificar palabras clave de exclusión
    if any(x in medio_norm for x in ["sports", "science", "daily galaxy", "espn", "marca", "olé"]):
        return "centro" # Asumimos centro/neutral para deportes/ciencia

    # Búsqueda exacta o parcial
    if medio_norm in media_sesgos:
        return media_sesgos[medio_norm]
    
    # Búsqueda parcial (si "Infobae Argentina" contiene "infobae")
    for key, value in media_sesgos.items():
        if key in medio_norm:
            return value
            
    return "desconocido"

def clasificar_titulo(titulo):
    if not titulo:
        return "indeterminado"
        
    titulo_norm = titulo.lower()
    
    palabras_clave = {
        "izquierda": [
            "igualdad", "derechos", "cambio climático", "progresista", "inclusión", 
            "sindicato", "trabajadores", "social", "género", "feminismo", "ddhh",
            "ajuste", "represión", "neoliberal", "fmi"
        ],
        "derecha": [
            "libertad", "mercado", "seguridad", "conservador", "patriotismo", 
            "inversión", "propiedad", "empresa", "déficit", "inflación", "cepo",
            "terrorismo", "orden", "policía"
        ],
        "centro": [
            "consenso", "neutralidad", "reforma", "diálogo", "moderación", 
            "equilibrio", "justicia", "transparencia", "acuerdo", "oficial",
            "anuncio", "informe", "reporte"
        ]
    }
    
    conteo = {"izquierda": 0, "derecha": 0, "centro": 0}
    
    for sesgo, palabras in palabras_clave.items():
        conteo[sesgo] = sum(1 for palabra in palabras if palabra in titulo_norm)
    
    # Retorna el sesgo con más coincidencias
    # Usamos una función lambda simple para evitar problemas de tipado
    max_sesgo = max(conteo, key=lambda k: conteo[k])
    
    if conteo[max_sesgo] > 0:
        return max_sesgo
    else:
        return "indeterminado"

def clasificar_noticia(medio, titulo):
    sesgo_medio = clasificar_sesgo(medio)
    sesgo_titulo = clasificar_titulo(titulo)
    
    # Lógica de decisión jerárquica
    
    # 1. Si el medio es conocido, su línea editorial suele pesar más
    if sesgo_medio != "desconocido":
        return sesgo_medio
        
    # 2. Si el medio es desconocido, intentamos por el título
    if sesgo_titulo != "indeterminado":
        return sesgo_titulo
        
    # 3. Si nada funciona, por defecto "centro" (para que se muestre en el filtro 'all' y 'center')
    return "centro"
