import tkinter as tk
from PIL import Image, ImageTk
from views.tablero import Tablero
import minmax

class Ventana_Juego(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Smart Horses")
        self.geometry("600x750")
        self.config(bg="white")
        self.cell_size = 50  # Size of each cell
        self.cells = []  # List to store references to the created cells

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
        self.botonPrincipiante = tk.Button(self, image=self.btnPrincipiante_img, bg="white", bd=0, command=lambda: self.nivel("1"))
        self.botonPrincipiante.pack()
        self.botonPrincipiante.place(x=250, y=150)

        self.botonAmateur = tk.Button(self, image=self.btnAmateur_img, bg="white", bd=0, command=lambda: self.nivel("2"))
        self.botonAmateur.pack()
        self.botonAmateur.place(x=370, y=150)

        self.botonExperto = tk.Button(self, image=self.btnExperto_img, bg="white", bd=0, command=lambda: self.nivel("3"))
        self.botonExperto.pack()
        self.botonExperto.place(x=480, y=150)

        # Canvas of the game board
        self.canvas = tk.Canvas(self, bg='blue')
        self.canvas.place(x=50, y=250, width=400, height=400)

        # Create the chessboard using the Tablero class
        self.cell_size = 50  # Size of each cell
        self.cells = []  # List to store references to the created cells
        tablero = Tablero(self.canvas, self.cell_size, self.cells)
        tablero.crear_tablero()

        # Boton reiniciar
        self.botonReinicio = tk.Button(self, image=self.btnReinicio_img, bg="white", bd=0, command=self.reiniciar_programa)
        self.botonReinicio.pack()
        self.botonReinicio.place(x=230, y=680)

    def reiniciar_programa(self):
        self.destroy()  # Close the current window
        minmax.generar_tablero(reset=True)
        Ventana_Juego()

    def generar_tablero_level(self, reset=True):
        global tableroGame, posicionJugadorMax, posicionJugadorMin
        tableroGame, posicionJugadorMax, posicionJugadorMin = minmax.obtener_tablero(reset=True)
        # Clear the canvas
        self.canvas.delete("all")

        # Create a new chessboard using the Tablero class
        tablero_obj = Tablero(self.canvas, self.cell_size, self.cells)
        tablero_obj.crear_tablero()

        # Update the game board with the generated numbers
        for i in range(8):
            for j in range(8):
                x = j * self.cell_size + self.cell_size // 2
                y = i * self.cell_size + self.cell_size // 2
                numero = tableroGame[i][j]
                if numero == 8:
                    img_caballoB = Image.open("resources/images/caballo_blanco.png")
                    img_caballoB = img_caballoB.resize((40, 40), Image.ANTIALIAS)
                    self.canvas.image_caballoB = ImageTk.PhotoImage(img_caballoB)
                    self.canvas.create_image(x, y, image=self.canvas.image_caballoB, tags="caballo_blanco")
                elif numero == 9:
                    img_caballoN = Image.open("resources/images/caballo_negro.png")
                    img_caballoN = img_caballoN.resize((40, 40), Image.ANTIALIAS)
                    self.canvas.image_caballoN = ImageTk.PhotoImage(img_caballoN)
                    self.canvas.create_image(x, y, image=self.canvas.image_caballoN, tags="caballo_negro")
                elif numero != 0:
                    self.canvas.create_text(x, y, text=str(numero), font=("Arial", 12))

        # Actualizar las coordenadas de los caballos
        self.posicion_caballoB = posicionJugadorMax
        self.posicion_caballoN = posicionJugadorMin

    def nivel(self, nivel):
        if nivel == "1":

            self.generar_tablero_level(reset=True)
            print(tableroGame)
            minmax.complejidad_juego('principiante')
            print("movimientosPosibles Max",  minmax.movimientos_posibles( tableroGame, 'Max'))
            print("movimientosPosibles Min",  minmax.movimientos_posibles( tableroGame, 'Min'))

        elif nivel == "2":
            pass
        elif nivel == "3":
            pass