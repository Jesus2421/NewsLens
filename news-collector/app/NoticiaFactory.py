import re
class Noticia:
    __slots__ = ('titulocompleto', 'titulo', 'medio', 'link', 'data_publicacion')

    def __init__(self, titulocompleto, link, data_publicacion):
        self.titulocompleto = titulocompleto  # Definir el atributo
        self.link = link
        self.titulo = None
        self.medio = None
        self.separar_titulo_y_medio()
        self.data_publicacion = data_publicacion

    def separar_titulo_y_medio(self):
        partes = self.titulocompleto.rsplit(" - ", 1)
        if len(partes) == 2:
            self.titulo, self.medio = partes[0].strip(), partes[1].strip()
        else:
            self.titulo = self.titulocompleto
            self.medio = None

    def __str__(self):
        return (f"Título: {self.titulo}\n"
                f"Medio: {self.medio}\n"
                f"Enlace: {self.link}\n"
                f"Fecha: {self.data_publicacion}\n")

class NoticiaFactory:
    @staticmethod
    def create_noticia(datos):
        noticias = []  # Inicializar la lista para almacenar las noticias
        for dato in datos:
            # Creamos una instancia de Noticia por cada entrada en datos_api
            noticia = Noticia(
                titulocompleto=dato.get("title"),  # Cambiado "tittle" a "title"
                link=dato.get("link"),
                data_publicacion=dato.get("pubDate")  # Asegúrate de usar 'data_publicacion'
            )
            noticias.append(noticia)  # Agregar la noticia a la lista
        return noticias
    