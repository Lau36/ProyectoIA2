import numpy as np
import tkinter as tk

class Tablero:
    def __init__(self, canvas, cell_size, cells):
        self.canvas = canvas
        self.cell_size = cell_size
        self.cells = cells

    def crear_tablero(self):
        for i in range(8):
            for j in range(8):
                x0 = j * self.cell_size
                y0 = i * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size
                color = "beige" if (i + j) % 2 == 0 else "gray"
                cell = self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
                self.cells.append(cell)

    def generar_tablero(self):
        tablero = np.zeros((8, 8), dtype=int)

        # Generar una lista de números del 1 al 7 (excluyendo el 8 y 9)
        numeros = list(range(1, 8))

        # Asignar los números en posiciones aleatorias del tablero sin superposición
        for num in numeros:
            while True:
                posicion = np.random.randint(8*8)
                fila, columna = np.unravel_index(posicion, (8, 8))
                if tablero[fila, columna] == 0:
                    tablero[fila, columna] = num
                    break

        # Asignar el número 8 en una posición aleatoria para representar el caballo blanco
        while True:
            posicion = np.random.randint(8*8)
            fila, columna = np.unravel_index(posicion, (8, 8))
            if tablero[fila, columna] == 0:
                tablero[fila, columna] = 8
                self.columna_caballoB = columna
                self.fila_caballoB = fila
                break

        # Asignar el número 9 en una posición aleatoria para representar el caballo negro
        while True:
            posicion = np.random.randint(8*8)
            fila, columna = np.unravel_index(posicion, (8, 8))
            if tablero[fila, columna] == 0:
                tablero[fila, columna] = 9
                self.posicion_caballoN = (columna, fila)
                break

        return tablero, self.columna_caballoB, self.fila_caballoB, self.posicion_caballoN
