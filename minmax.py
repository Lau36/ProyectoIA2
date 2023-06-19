# from nodo import Nodo
# from tablero import tablero
import numpy as np

# Variables globales --------------------------------------------------------------------------------------------------------------------------------------------------
# tableroGame = np.zeros((8, 8), dtype=int)
jugadorGame = 'Max'
puntajeMin = 0
puntajeMax = 0
posicionJugadorMax = []
posicionJugadorMin = []
tableroGame = np.array([
    [0, 0, 0, 0, 0, 4, 0, 0],
    [0, 0, 1, 0, 0, 0, 9, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 3, 0, 0, 0],
    [0, 8, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 6, 0, 0, 0],
    [0, 0, 5, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
])

# Funciones auxiliares -------------------------------------------------------------------------------------------------------------------------------------------------


def complejidad_juego(nivelFront):
    if nivelFront == 'principiante':
        profundidadGame = 2
    if nivelFront == 'amateur':
        profundidadGame = 4
    if nivelFront == 'experto':
        profundidadGame = 6
    return profundidadGame


def generar_tablero(reset=False):
    global tableroGame, posicionJugadorMax, posicionJugadorMin
    if reset or np.count_nonzero(tableroGame) == 0:
        tableroGame = np.zeros((8, 8), dtype=int)  # Reinicia el tablero
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
                posicionJugadorMax = (columna, fila)
                break

        # Asignar el número 9 en una posición aleatoria para representar el caballo negro(Humano)
        while True:
            posicion = np.random.randint(8*8)
            fila, columna = np.unravel_index(posicion, (8, 8))
            if tableroGame[fila, columna] == 0:
                tableroGame[fila, columna] = 9
                posicionJugadorMin = (columna, fila)
                break

    return tableroGame, posicionJugadorMax, posicionJugadorMin

# Alamcena el tablero


def obtener_tablero(reset=False):
    global tableroGame, posicionJugadorMax, posicionJugadorMin
    if reset or np.count_nonzero(tableroGame) == 0:
        tableroGame, posicionJugadorMax, posicionJugadorMin = generar_tablero(
            reset=True)
    return tableroGame, posicionJugadorMax, posicionJugadorMin


# WARNING Mejorar esta función
def juego_terminado(tablero):
    numeros = list(range(1, 8))
    terminado = False
    for fila in tablero:
        for numero in fila:
            if numero in numeros:
                return False  # aqui mira que no todos los numeros del tablero son diferentes de 1 a 7
    return True

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
            if alcanzar_casilla(tablero, jugador, fila, columna):
                jugada = (fila, columna)
                jugadas_posibles.append(jugada)
    return jugadas_posibles

# Verifica si el caballo puede alcanzar una posicion


def alcanzar_casilla(tablero, jugador, fila, columna):
    # obtiene la posicion actual del caballo del jugador
    posicionActual = obtener_posicion_caballo(tablero, jugador)
    if posicionActual is None:
        return False
    if tablero[fila][columna] != 9 and tablero[fila][columna] != 8:
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
    global puntajeMin, puntajeMax

    new = tablero.copy()
    fila, columna = jugada[0], jugada[1]  # Obtener fila y columna de la jugada

    # Verifica si en esa casilla hay un punto
    if casilla_puntos(tablero, fila, columna):
        puntaje = tablero[fila][columna]  # Corrección aquí
        sumar_puntaje(jugador, puntaje)
        print("El puntaje que lleva es:", sumar_puntaje(jugador, puntaje))

    if jugador == 'Max':
        new[fila, columna] = 8
    if jugador == 'Min':
        new[fila, columna] = 9

    return new


def sumar_puntaje(jugador, puntuacion):
    global puntajeMin, puntajeMax
    if jugador == 'Max':
        puntajeMax += puntuacion
        return puntajeMax
    if jugador == 'Min':
        puntajeMin += puntuacion
        return puntajeMin


# Aqui sabemos a quien le toca el turno si el jugador ya es max, pasaria a ser min


def oponente(jugador):
    if jugador == 'Max':
        jugador = 'Min'
    else:
        jugador = 'Max'


def evaluar_estado(puntajeMax, puntajeMin):
    utilidad = puntajeMax - puntajeMin
    return utilidad

# MiniMax --------------------------------------------------------------------------------------------------------------------------------------------


def minimax(tablero, jugador, profundidad, alfa, beta):
    if profundidad == 0 or juego_terminado(tablero):
        # aqui deberia de retornar la utilidad final
        return evaluar_estado(puntajeMax, puntajeMin)

    if jugador == 'Max':
        # Esto es un infinito con numero negativos
        mejorValor = float("-inf")
        movimientos = movimientos_posibles(tablero, jugador)
        for jugada in movimientos:
            nuevoTablero = realizarJugada(tablero, jugada, jugador)
            valor = minimax(
                nuevoTablero, oponente(jugador), profundidad - 1)
            mejorValor = max(mejorValor, valor)
            alfa = max(alfa, mejorValor)
            if beta <= alfa:
                break  # Poda alfa-beta
        return mejorValor

    else:
        # Esto es un infinito con numero negativos
        mejorValor = float("inf")
        for jugada in movimientos_posibles(tablero, jugador):
            nuevoTablero = realizarJugada(tablero, jugada, jugador)
            valor = minimax(
                nuevoTablero, oponente(jugador), profundidad - 1)
            mejorValor = min(mejorValor, valor)
            beta = min(beta, mejorValor)
            if beta <= alfa:
                break  # Poda alfa-beta
        return mejorValor


def verificar_primer_movimiento_max(tablero, profundidad, jugador):
    movimientos_iniciales = movimientos_posibles(tablero, jugador)
    mejor_utilidad = float('-inf')
    alfa = float("-inf")
    beta = float("inf")
    mejor_movimiento = None

    for movimiento in movimientos_iniciales:
        nuevo_tablero = realizarJugada(tablero, movimiento, jugador)
        utilidad = minimax(nuevo_tablero, oponente(
            jugador), profundidad, alfa, beta)
        if utilidad > mejor_utilidad:
            mejor_utilidad = utilidad
            mejor_movimiento = movimiento

    return mejor_movimiento


print(tableroGame)
# aiuda esto no está dando lo que necesito :(
print("jugada", verificar_primer_movimiento_max(tableroGame, 4, jugadorGame))

# print("puntaje", sumar_puntaje('Max', 5))
# print("como sigue el tablero", tableroGame)
# print("El pruntaje en max", puntajeMax)
# # print("tablero min", obtener_tablero(reset=True))
# # print("tablero max", obtener_tablero(reset=True))
# # print("movimientosPosibles Max", movimientos_posibles(tableroGame, 'Max'))
# # print("movimientosPosibles Min", movimientos_posibles(tableroGame, 'Min'))
