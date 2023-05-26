import tkinter as tk
from PIL import Image, ImageTk

class Ventana_Juego(tk.Toplevel):
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

        # Imagenes de niveles
        # Carga la imagen nivel principiante
        imagePrincipiante = Image.open("resources/images/level_principiante.png")
        imagePrincipiante = imagePrincipiante.resize((100, 50))  # Ajusta el tamaño de la imagen si es necesario
        self.btnPrincipiante_img = ImageTk.PhotoImage(imagePrincipiante)

        # Carga la imagen nivel amateur
        imageAmateur = Image.open("resources/images/level_amateur.png")
        imageAmateur = imageAmateur.resize((100, 50))  # Ajusta el tamaño de la imagen si es necesario
        self.btnAmateur_img = ImageTk.PhotoImage(imageAmateur)

        # Carga la imagen nivel experto
        imageExperto = Image.open("resources/images/level_experto.png")
        imageExperto = imageExperto.resize((100, 50))  # Ajusta el tamaño de la imagen si es necesario
        self.btnExperto_img = ImageTk.PhotoImage(imageExperto)

        # Carga la imagen nivel experto
        imageReiniciar = Image.open("resources/images/reiniciar.png")
        imageReiniciar = imageReiniciar.resize((100, 50))  # Ajusta el tamaño de la imagen si es necesario
        self.btnReinicio_img = ImageTk.PhotoImage(imageReiniciar)

        # Nivel de dificultad
        self.difficultLabel = tk.Label(self, text="Escoge la dificultad del juego: ")
        self.difficultLabel.pack()
        self.difficultLabel.config(font=('Times New Roman', 12), bg="white")
        self.difficultLabel.place(x=50, y=160)

        # Botones de dificultad
        self.botonPrincipiante = tk.Button(self, image=self.btnPrincipiante_img, bg="white",bd=0 , command= lambda: self.nivel("1"))
        self.botonPrincipiante.pack()
        self.botonPrincipiante.place(x= 250, y= 150)

        self.botonAmateur = tk.Button(self, image=self.btnAmateur_img, bg="white",bd=0, command= lambda: self.nivel("2"))
        self.botonAmateur.pack()
        self.botonAmateur.place(x= 370, y= 150)

        self.botonExperto = tk.Button(self, image=self.btnExperto_img, bg="white",bd=0, command= lambda: self.nivel("3"))
        self.botonExperto.pack()
        self.botonExperto.place(x= 480, y= 150)

        # Canvas de tablero
        self.canvas = tk.Canvas(self, bg='blue')
        self.canvas.place(x=50, y= 250, width=300, height=330)

        def reiniciar_programa(self):
            self.destroy()  # Cierra la ventana actual
            Ventana_Juego()  # Abre una nueva ventana

        # Boton reiniciar
        self.botonReinicio = tk.Button(self, image=self.btnReinicio_img, bg="white",bd=0, command=reiniciar_programa)
        self.botonReinicio.pack()
        self.botonReinicio.place(x= 420, y= 520)

    def nivel(self,nivel):
        if nivel=="1":
            pass
        elif nivel=="2":
            pass
        elif nivel=="3":
            pass

    