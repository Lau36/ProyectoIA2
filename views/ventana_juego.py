import tkinter as tk
from PIL import Image, ImageTk
from views.tablero import Tablero
import minmax
import copy

class Ventana_Juego(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Smart Horses")
        self.geometry("600x750")
        self.config(bg="white")
        self.cell_size = 50  # Size of each cell
        self.cells = []  # List to store references to the created cells
        self.PosiblesmovimientosMin = []  # List to store possible moves for the black horse

        # Imagen de título
        img = Image.open("resources/images/Smart Horses.png")
        img = img.resize((610, 200))  # Resize the image
        self.photo = ImageTk.PhotoImage(img)
        self.tituloHorses = tk.Label(self, image=self.photo)
        self.tituloHorses.pack(pady=10)
        self.tituloHorses.config(bg="white")
        self.tituloHorses.place(x=0, y=0)

        # Imágenes de niveles
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

        # Canvas de juego
        self.canvas = tk.Canvas(self, bg='blue')
        self.canvas.place(x=50, y=250, width=400, height=400)
        tablero = Tablero(self.canvas, self.cell_size, self.cells)
        tablero.crear_tablero()

        # Boton reiniciar
        self.botonReinicio = tk.Button(self, image=self.btnReinicio_img, bg="white", bd=0, command=self.reiniciar_programa)
        self.botonReinicio.pack()
        self.botonReinicio.place(x=230, y=680)

    # Función que reinicia la ventana_juego
    def reiniciar_programa(self):
        self.destroy()  # Destruye le ventana actual
        # minmax.generar_tablero(reset=True)
        Ventana_Juego() # Vuelve a llamar la misma clase, es decir todo lo que contiene

    # Funcioón que muestra las posibles jugadas dibujadas en el tablero de juego
    def mostrar_posibles_jugadas(self, posibles_jugadas):
        for i, j in posibles_jugadas:
            x = j * self.cell_size + self.cell_size // 2
            y = i * self.cell_size + self.cell_size // 2
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, outline="green", width=2)

    # Esta funcón genera el tablero con el que se va a jugar 
    def generar_tablero_level(self, reset=True):
        global tableroGame, posicionJugadorMax, posicionJugadorMin # Variables globales

        tableroGame, posicionJugadorMax, posicionJugadorMin = minmax.obtener_tablero(reset=True) # Obtengo el tablero generado en minmax
        
        # Limpio el canvas previo
        self.canvas.delete("all")

        # Creo el nuevo tablero
        tablero_obj = Tablero(self.canvas, self.cell_size, self.cells)
        tablero_obj.crear_tablero()

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

        self.posicion_caballoB = posicionJugadorMax
        self.posicion_caballoN = posicionJugadorMin

        self.PosiblesmovimientosMin = minmax.movimientos_posibles(tableroGame, 'Min')

    def mover_caballo_negro(self, event):
        global tableroGame
        x = event.x
        y = event.y
        i = y // self.cell_size
        j = x // self.cell_size

        # Crear una copia del tablero actual
        tableroGame_copia = copy.deepcopy(tableroGame)

        if (i, j) in self.PosiblesmovimientosMin:
            # Eliminar el número 9 de la posición anterior del caballo negro en la copia del tablero
            tableroGame_copia[self.posicion_caballoN[0]][self.posicion_caballoN[1]] = 0

            # Actualizar la posición del caballo negro en la copia del tablero
            tableroGame_copia[i][j] = 9

            # Actualizar la posición del caballo negro en la variable de clase
            self.posicion_caballoN = (i, j)

            # Limpiar el lienzo
            self.canvas.delete("all")

            # Recrear el tablero de ajedrez utilizando la clase Tablero
            tablero_obj = Tablero(self.canvas, self.cell_size, self.cells)
            tablero_obj.crear_tablero()

            # Actualizar el tablero de juego con los números generados
            for i in range(8):
                for j in range(8):
                    x = j * self.cell_size + self.cell_size // 2
                    y = i * self.cell_size + self.cell_size // 2
                    numero = tableroGame_copia[i][j]
                    if numero == 8:
                        # Dibujar la imagen del caballo blanco
                        img_caballoB = Image.open("resources/images/caballo_blanco.png")
                        img_caballoB = img_caballoB.resize((40, 40), Image.ANTIALIAS)
                        self.canvas.image_caballoB = ImageTk.PhotoImage(img_caballoB)
                        self.canvas.create_image(x, y, image=self.canvas.image_caballoB, tags="caballo_blanco")
                    elif numero == 9:
                        # Dibujar la nueva imagen del caballo negro en la posición actualizada
                        img_caballoN = Image.open("resources/images/caballo_negro.png")
                        img_caballoN = img_caballoN.resize((40, 40), Image.ANTIALIAS)
                        self.canvas.image_caballoN = ImageTk.PhotoImage(img_caballoN)
                        self.canvas.create_image(x, y, image=self.canvas.image_caballoN, tags="caballo_negro")
                    elif numero != 0:
                        self.canvas.create_text(x, y, text=str(numero), font=("Arial", 12))

            # Eliminar la imagen del caballo negro anterior
            self.canvas.delete("caballo_negro")

            # Actualizar la posición del caballo negro
            self.posicionJugadorMin = (i, j)

            # Obtener los nuevos movimientos posibles para el caballo negro
            self.PosiblesmovimientosMin = minmax.movimientos_posibles(tableroGame_copia, 'Min')

            # Mostrar los nuevos movimientos posibles en el tablero
            self.mostrar_posibles_jugadas(self.PosiblesmovimientosMin)

            # Actualizar el tablero de juego con el nuevo estado
            tableroGame = tableroGame_copia
            print("Copy tablero: ", tableroGame_copia)
            print("Tablero supuestamente actual: ", tableroGame)

    def nivel(self, nivel):
        if nivel == "1":
            self.generar_tablero_level(reset=True)
            print(tableroGame)  # Imprimir el tablero actualizado
            self.mostrar_posibles_jugadas(self.PosiblesmovimientosMin)
            self.canvas.bind("<Button-1>", self.mover_caballo_negro)
        elif nivel == "2":
            pass
        elif nivel == "3":
            pass