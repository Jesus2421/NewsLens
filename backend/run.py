# Programa Principal
from app import utils
# vamos hacer una interfaz grafica
from tkinter import *
 # Creamos la ventana principal
ventana_principal = Tk()
ventana_principal.title("Noticias del Mundo")
ventana_principal.iconbitmap("imagenes/news.ico")
ventana_principal.resizable(0,0)
ventana_principal.config(bg="white")
ContenerdorNoticias = Frame()
ContenerdorNoticias.pack()
ContenerdorNoticias.config(bg="light grey")
ContenerdorNoticias.config(width="1000",height="1000")
def open_link(Enlace):
         import webbrowser
         webbrowser.open(Enlace)
def main():
    noticias = utils.get_google_news()
    for noticia in noticias:
        cadena = noticia['title']
        partes = cadena.split(" - ", maxsplit=1)
        titulo = partes[0]
        periodico = partes[1] if len(partes) > 1 else "Nombre del periódico no disponible"
        Enlace = noticia['link']
        # creamos un label para mostrar la noticia
        label = Label(ContenerdorNoticias, text=titulo, bg="light grey")
        BotonEnlace = Button(ContenerdorNoticias,text=periodico, command=lambda link=Enlace: open_link(link))
        label.pack()
        BotonEnlace.pack()



if __name__ == '__main__':
    main()
    ventana_principal.mainloop()







