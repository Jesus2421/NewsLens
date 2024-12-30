from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report
import pandas as pd
from app.NoticiaFactory import NoticiaFactory
# Ejemplo de datos
Noticias = NoticiaFactory().getNoticias()
data = {
    'title': [
        'Perimenopause, standing desks and service dogs: The week in Well+Being',
        'Experts say daily "sitting down limit" can ward off heart attacks'
    ],
    'source': ['The Washington Post', 'Daily Mail'],
    'label': ['Health', 'Health']  # Ejemplo de etiqueta de "cámara de eco"
}