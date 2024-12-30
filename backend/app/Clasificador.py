def clasificar_sesgo(medio):
    media_sesgos = {
        "The Wall Street Journal":"centro-derecha",
        "ABC7 Los Angeles":"Centro",
        "The Hill":"Centro-Derech",
        "IGN":"Neutral",
        "The Globe and Mail":"centro-izquierda",
        "Deadline":"Neutral",
        "Good News Network":"Neutral",
        "Reuters.com": "Centro",
        "engadget":"neutral",
        "haaretz":"izquierda",
        "The Associated Press":"neutral",
        "ABC News":"centro",
        "Politico":"centro",
        "POLITICO Europe":"centro",
        "Shore Daily News":"derecha",
        "New York Post": "derecha",
        "SciTechDaily": "neutral",
        "The New York Times": "centro",
        "The Washington Post":"centro",
        "Fox News": "derecha",
        "Axios":"centro",
        "Forbes": "derecha",
        "CNN": "izquierda",
        "BBC.com": "centro",
        "The Verge" :"centro",
        "Al Jazeera": "centro",
        "The Guardian": "izquierda",
        "Wall Street Journal": "derecha",
    }
    # Verificar si el nombre del medio contiene "Sports" (ignorando mayúsculas y minúsculas)
    if "sports" in medio.lower() or "science" in medio.lower() or "The daily galaxy" in medio.lower():
        return "No es un medio con un sesgo politico claro"
    return media_sesgos.get(medio, "desconocido")  # Retorna "desconocido" si el medio no está en el mapeo

def clasificar_titulo(titulo):
    palabras_clave = {
        "izquierda": ["igualdad", "derechos", "cambio climático", "progresista", "inclusión"],
        "derecha": ["libertad", "mercado", "seguridad", "conservador", "patriotismo"],
        "centro": ["consenso", "neutralidad", "reforma", "diálogo", "moderación", "equilibrio", "justicia", "transparencia"]
    }
    conteo = {"izquierda": 0, "derecha": 0}
    
    for sesgo, palabras in palabras_clave.items():
        conteo[sesgo] = sum(1 for palabra in palabras if palabra.lower() in titulo.lower())
    
    # Retorna el sesgo con más coincidencias
    if conteo["izquierda"] > conteo["derecha"]:
        return "izquierda"
    elif conteo["derecha"] > conteo["izquierda"]:
        return "derecha"
    else:
        return "indeterminado"  # Si hay empate o no hay coincidencias
    
def clasificar_noticia(medio, titulo):
        sesgo_medio = clasificar_sesgo(medio)
        sesgo_titulo = clasificar_titulo(titulo)
        # Si ambos coinciden, usa ese sesgo
        if sesgo_medio == sesgo_titulo:
            return sesgo_medio
        # Si no coinciden, prioriza el sesgo del medio
        if sesgo_medio != "desconocido":
            return sesgo_medio
        # Si el medio es desconocido, usa el sesgo del título
        return sesgo_titulo


