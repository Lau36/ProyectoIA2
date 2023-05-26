import tkinter as tk
from PIL import Image, ImageTk
from views.ventana_juego import Ventana_Juego

class Ventana_Inicial(tk.Tk):


    def __init__(self):
        super().__init__()
        self.title("Smart Horses")
        self.geometry("600x600")
        self.config(bg="white")

        # Imagen de titulo
        img = Image.open("resources/images/Smart Horses.png")
        img = img.resize((610, 200))  # Resize the image
        self.photo = ImageTk.PhotoImage(img)
        self.tituloHorses = tk.Label(self, image=self.photo)
        self.tituloHorses.pack(pady=10)
        self.tituloHorses.config(bg="white")
        self.tituloHorses.place(x=0, y=0)

        # Carga la imagen jugar
        imageJugar = Image.open("resources/images/jugar.png")
        imageJugar = imageJugar.resize((200, 100))  # Ajusta el tamaño de la imagen si es necesario
        self.btnJugar_img = ImageTk.PhotoImage(imageJugar)

        # Carga la imagen creditos
        imageCreditos = Image.open("resources/images/creditos.png")
        imageCreditos = imageCreditos.resize((200, 100))  # Ajusta el tamaño de la imagen si es necesario
        self.btnCreditos_img = ImageTk.PhotoImage(imageCreditos)

        def juego():
            ventana_game = Ventana_Juego()
        
        def creditos():
            ventana_creditos = tk.Toplevel(self)
            ventana_creditos.title("Créditos")
            ventana_creditos. geometry("300x200")
            ventana_creditos.config(bg="white")

            # Crear una etiqueta para mostrar los créditos del programa
            etiqueta_creditos = tk.Label(
                ventana_creditos, text="Créditos \n  \n Laura Daniela Jaimes - 2040430 \n Diana Marcela Cadena - 2041260 \n Mayra Alejandra Sanchez - 2040506")
            etiqueta_creditos.pack()
            etiqueta_creditos.config(font=('Times New Roman', 10), bg="white")
            etiqueta_creditos.place(x=50, y=50)

        # Crea el botón con la imagen jugar y creditos
        self.botonJugar = tk.Button(self, image=self.btnJugar_img, bg="white", bd=0, command=juego)
        self.botonJugar.pack()
        self.botonJugar.place(x= 200, y= 200)
        
        self.botonCreditos = tk.Button(self, image=self.btnCreditos_img, bg="white",bd=0, command=creditos)
        self.botonCreditos.pack()
        self.botonCreditos.place(x= 200, y= 350)

        # Hacer boton para detener y reiniciar el sonido
