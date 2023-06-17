import numpy as np
import tkinter as tk

def generar_tablero():
    tablero = np.zeros((8, 8), dtype=int)

    # Generar una lista de números del 1 al 9
    numeros = list(range(1, 10))

    # Asignar los números en posiciones aleatorias del tablero sin superposición
    for num in numeros:
        while True:
            posicion = np.random.randint(8*8)
            fila, columna = np.unravel_index(posicion, (8, 8))
            if tablero[fila, columna] == 0:
                tablero[fila, columna] = num
                if num == 8:
                    # posicion_caballoB =(columna,fila)
                    columna_caballoB = columna
                    fila_caballoB = fila
                elif num == 9:
                    posicion_caballoN =(columna,fila)
                break
               
    return tablero, columna_caballoB, fila_caballoB, posicion_caballoN

class Tablero:
    def __init__(self, tablero, columna_caballoB, fila_caballoB, posicion_caballoN):
        self.tablero = tablero
        self.columna_caballoB = columna_caballoB
        self.fila_caballoB = fila_caballoB
        self.posicion_caballoN = posicion_caballoN

    def dibujar_tablero(self):
        ventana = tk.Tk()
        ventana.title("Tablero de Ajedrez")

        lienzo = tk.Canvas(ventana, width=400, height=400)
        lienzo.pack()

        for i in range(8):
            for j in range(8):
                x0 = j * 50
                y0 = i * 50
                x1 = x0 + 50
                y1 = y0 + 50
                color = "white" if (i + j) % 2 == 0 else "gray"
                lienzo.create_rectangle(x0, y0, x1, y1, fill=color)
                if self.tablero[i, j] != 0:
                    lienzo.create_text(x0 + 25, y0 + 25, text=str(self.tablero[i, j]), font=("Arial", 20))

        ventana.mainloop()

tablero, columna_caballoB, fila_caballoB, posicion_caballoN = generar_tablero()
objeto_tablero = Tablero(tablero, columna_caballoB, fila_caballoB, posicion_caballoN)
objeto_tablero.dibujar_tablero()