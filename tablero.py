import numpy as np


class tablero:
    def __init__(self, matriz, posNumeros):
        self.matriz = matriz,
        self.posNumeros = posNumeros,

    def generar_tablero(self):
        # self.matriz = np.zeros((8, 8), dtype=int)
        # Generar una lista de números del 1 al 9
        numeros = list(range(1, 10))

    # Asignar los números en posiciones aleatorias del self.matriz sin superposición
        for num in numeros:
            while True:
                posicion = np.random.randint(8*8)
                fila, columna = np.unravel_index(posicion, (8, 8))
                if self.matriz[fila, columna] == 0:
                    self.matriz[fila, columna] = num
                    break
        return self.matriz

    def juego_terminado(self):
        terminado = False
        for fila in self.matriz:
            for casilla in fila:
                if casilla == 0:
                    terminado = True
                    return terminado
                else:
                    terminado = False

    def casillas_posibles(self):
        1
