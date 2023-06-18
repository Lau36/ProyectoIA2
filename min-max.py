from nodo import Nodo
from tablero import tablero
import numpy as np
import random

# Variables globales --------------------------------------------------------------------------------------------------------------------------------------------------
tableroGame = np.zeros((8, 8), dtype=int)
jugadorGame = 'Max'
posicionJugadorMax = []
posicionJugadorMin = []
# tableroGame = np.array([
#     [0, 0, 0, 0, 0, 4, 0, 0],
#     [0, 0, 1, 0, 0, 0, 9, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 7, 0, 0, 3, 0, 0, 0],
#     [0, 8, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 6, 0, 0, 0],
#     [0, 0, 5, 0, 0, 0, 2, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0]
# ])

# Funciones auxiliares -------------------------------------------------------------------------------------------------------------------------------------------------

# Función que define la complejidad del juego


def complejidad_juego(nivelFront):
    if nivelFront == 'principiante':
        profundidadGame = 2
    if nivelFront == 'amateur':
        profundidadGame = 4
    if nivelFront == 'experto':
        profundidadGame = 6
    return profundidadGame


def generar_tablero():
    numeros = list(range(1, 8))
    for num in numeros:
        while True:
            posicion = np.random.randint(8*8)
            fila, columna = np.unravel_index(posicion, (8, 8))
            if tableroGame[fila, columna] == 0:
                tableroGame[fila, columna] = num
                break
    # Asignar el número 8 en una posición aleatoria para representar el caballo blanco(IA)
    while True:
        posicion = np.random.randint(8*8)
        fila, columna = np.unravel_index(posicion, (8, 8))
        if tableroGame[fila, columna] == 0:
            tableroGame[fila, columna] = 8
            columna_Max = columna
            fila_Max = fila
            break

        # Asignar el número 9 en una posición aleatoria para representar el caballo negro(Humano)
    while True:
        posicion = np.random.randint(8*8)
        fila, columna = np.unravel_index(posicion, (8, 8))
        if tableroGame[fila, columna] == 0:
            tableroGame[fila, columna] = 9
            posicionJugadorMin = (columna, fila)
            break
    return tableroGame, columna_Max, fila_Max, posicionJugadorMin


# WARNING Mejorar esta función
def juego_terminado(tablero):
    terminado = False
    for fila in tablero:
        for casilla in fila:
            if casilla == 0:
                terminado = True
                return terminado
            else:
                terminado = False

# Calcula si en esa casilla hay un elemento punto


def casilla_puntos(tablero, fila, columna):
    if tablero[fila][columna] == 1:
        return True
    if tablero[fila][columna] == 2:
        return True
    if tablero[fila][columna] == 3:
        return True
    if tablero[fila][columna] == 4:
        return True
    if tablero[fila][columna] == 5:
        return True
    if tablero[fila][columna] == 6:
        return True
    if tablero[fila][columna] == 7:
        return True
    else:
        return False

# Calcula los movimientos posibles y los pone en una lista de jugadas posibles


def movimientos_posibles(tablero, jugador):
    jugadas_posibles = []
    for fila in range(8):
        for columna in range(8):
            # Pregunto si en esa fila y columna hay un punto
            if casilla_puntos(tablero, fila, columna):
                # Verifica que el caballo del jugador pueda alcanzar la casilla
                if alcanzar_casilla(tablero, jugador, fila, columna):
                    jugada = (fila, columna)
                    jugadas_posibles.append(jugada)
    return jugadas_posibles

# Verifica si el caballo puede alcanzar una posicion


def alcanzar_casilla(tablero, jugador, fila, columna):
    # obtiene la posicion actual del caballo del jugador
    posicionActual = obtener_posicion_caballo(tablero, jugador)
    distanciaFila = abs(fila - posicionActual[0])
    distanciaColumna = abs(columna - posicionActual[1])
    if (distanciaFila == 2 and distanciaColumna == 1) or (distanciaFila == 1 and distanciaColumna == 2):
        return True
    else:
        return False

# Funcion que obtiene la posicion del caballo


def obtener_posicion_caballo(tablero, jugador):
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if jugador == 'Max':
                if tablero[i][j] == 8:
                    return (i, j)
            if jugador == 'Min':
                if tablero[i][j] == 9:
                    return (i, j)


def realizarJugada(tablero, jugada, jugador):
    pass
    # if casilla_puntos(tablero, jugada[0], jugada[1]):
    #     puntaje = tablero[0][1] #aca tendria que sacarme que hay en esa posicion


print("Tablero del juego", generar_tablero())
print("Tablero del juego", tableroGame)
print("movimientosPosibles", movimientos_posibles(tableroGame, 'Max'))

# MiniMax --------------------------------------------------------------------------------------------------------------------------------------------


def minimax(tablero, jugador, profundidad):
    if juego_terminado():
        return 1  # aqui deberia de retornar la utilidad final

    if jugador == 'Max':
        # Esto es un infinito con numero negativos
        mejorPuntaje = float("-inf")
        for jugada in movimientos_posibles():
            nuevoTablero = realizarJugada(tablero, jugada, jugador)
            puntuacion = minimax(
                nuevoTablero, oponente(jugador), profundidad - 1)
            mejorPuntuacion = max(mejorPuntaje, puntuacion)
        return mejorPuntuacion

# Aqui sabemos a quien le toca el turno si el jugador ya es max, pasaria a ser min


def oponente(jugador):
    if jugador == 'Max':
        jugador = 'Min'
    if jugador == 'Min':
        jugador = 'Min'

# abria que implementar algo en donde se pueda comunicar el front con los algoritmos para que pueda mostrar del humano, el estado actual (coordenadas) para saber que movimientos podria hacer


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
