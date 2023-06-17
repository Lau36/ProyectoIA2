from nodo import Nodo
from tablero import tablero
import numpy as np
import random

tableroGame = np.zeros((8, 8), dtype=int)
posicionJugadorMax = []
posicionJugadorMin = []


def generar_tablero():
    numeros = list(range(1, 8))
    for num in numeros:
        while True:
            posicion = np.random.randint(8*8)
            fila, columna = np.unravel_index(posicion, (8, 8))
            if tableroGame[fila, columna] == 0:
                tableroGame[fila, columna] = num
                break
    # Asignar el número 8 en una posición aleatoria para representar el caballo blanco
    while True:
        posicion = np.random.randint(8*8)
        fila, columna = np.unravel_index(posicion, (8, 8))
        if tableroGame[fila, columna] == 0:
            tableroGame[fila, columna] = 8
            columna_Max = columna
            fila_Max = fila
            break

        # Asignar el número 9 en una posición aleatoria para representar el caballo negro
    while True:
        posicion = np.random.randint(8*8)
        fila, columna = np.unravel_index(posicion, (8, 8))
        if tableroGame[fila, columna] == 0:
            tableroGame[fila, columna] = 9
            posicionJugadorMin = (columna, fila)
            break
    return tableroGame, columna_Max, fila_Max, posicionJugadorMin


def juego_terminado(tablero):
    terminado = False
    for fila in tablero:
        for casilla in fila:
            if casilla == 0:
                terminado = True
                return terminado
            else:
                terminado = False


def utilidad():
    1


# tableroGame = tablero(
#     np.zeros((8, 8), dtype=int),
#     []
# )
generar_tablero()
print("Tablero del juego", generar_tablero())
# print("terminado?", juego_terminado(tableroGame))

# def minimax(matriz_juego):
#     1
#     turno = False
# Jugador = ('Max')
# casillas_puntos = []
# nodos_creados = 0
# nodos_expandidos = 0

# raiz = Nodo(
# )

# pila = [raiz]

# while len(pila) > 0:
#     nodo = pila.pop()
#     nodos_expandidos += 1
#     if (nodo.condicionGanar[1]):
#         ganador = nodo.condicionGanar[0]
#         return ganador, nodo.puntosMaquina, nodo.puntosJugador

#     else:
#         return "Continuara..."

#     # genero los hijos

# return "No hay solucion", matriz_juego
