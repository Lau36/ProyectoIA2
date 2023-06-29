import numpy as np
from nodo import Nodo
import copy
import math

class Juego:
    def __init__(self):
        self.tableroGame = np.zeros((8, 8), dtype=int)
        self.jugadorGame = 'Max'
        self.puntajeMin = 0
        self.puntajeMax = 0
        self.posicionJugadorMax = []
        self.posicionJugadorMin = []

    def complejidad_juego(self, nivelFront):
        if nivelFront == 'principiante':
            profundidadGame = 2
        elif nivelFront == 'amateur':
            profundidadGame = 4
        elif nivelFront == 'experto':
            profundidadGame = 6
        return profundidadGame

    def generar_tablero(self, reset=False):
        if reset or np.count_nonzero(self.tableroGame) == 0:
            self.tableroGame = np.zeros((8, 8), dtype=int)
            numeros = list(range(1, 8))

            for num in numeros:
                while True:
                    posicion = np.random.randint(8*8)
                    fila, columna = np.unravel_index(posicion, (8, 8))
                    if self.tableroGame[fila, columna] == 0:
                        self.tableroGame[fila, columna] = num
                        break

            while True:
                posicion = np.random.randint(8*8)
                fila, columna = np.unravel_index(posicion, (8, 8))
                if self.tableroGame[fila, columna] == 0:
                    self.tableroGame[fila, columna] = 8
                    self.posicionJugadorMax = (columna, fila)
                    break

            while True:
                posicion = np.random.randint(8*8)
                fila, columna = np.unravel_index(posicion, (8, 8))
                if self.tableroGame[fila, columna] == 0:
                    self.tableroGame[fila, columna] = 9
                    self.posicionJugadorMin = (columna, fila)
                    break

        return self.tableroGame, self.posicionJugadorMax, self.posicionJugadorMin

    def obtener_tablero(self, reset=False):
        if reset or np.count_nonzero(self.tableroGame) == 0:
            self.tableroGame, self.posicionJugadorMax, self.posicionJugadorMin = self.generar_tablero(reset=True)
        return self.tableroGame, self.posicionJugadorMax, self.posicionJugadorMin

    def juego_terminado(self, tablero):
        numeros = list(range(1, 8))
        terminado = False
        for fila in tablero:
            for numero in fila:
                if numero in numeros:
                    return False
        return True

    def casilla_puntos(self, tablero, fila, columna):
        if tablero[fila][columna] in [1, 2, 3, 4, 5, 6, 7]:
            return True
        else:
            return False
        
    def movimientos_posibles(self, tablero, jugador):
        jugadas_posibles = []
        posiciones_visitadas = set()

        def buscar_movimiento(fila, columna, fila_anterior, columna_anterior):
            if fila < 0 or fila >= 8 or columna < 0 or columna >= 8 or (fila, columna) in posiciones_visitadas:
                return
            posiciones_visitadas.add((fila, columna))
            if self.alcanzar_casilla(tablero, jugador, fila, columna):
                jugada = (fila, columna)
                jugadas_posibles.append(jugada)
            else:
                # Evitar volver a la posición anterior inmediatamente
                if fila != fila_anterior or columna != columna_anterior:
                    buscar_movimiento(fila - 1, columna, fila, columna)  # Movimiento hacia arriba
                    buscar_movimiento(fila + 1, columna, fila, columna)  # Movimiento hacia abajo
                    buscar_movimiento(fila, columna - 1, fila, columna)  # Movimiento hacia la izquierda
                    buscar_movimiento(fila, columna + 1, fila, columna)  # Movimiento hacia la derecha

        posicionActual = self.obtener_posicion_caballo(tablero, jugador)
        if posicionActual is not None:
            buscar_movimiento(posicionActual[0], posicionActual[1], -1, -1)  # -1, -1 para evitar la posición anterior

        return jugadas_posibles

    def alcanzar_casilla(self, tablero, jugador, fila, columna):
        posicionActual = self.obtener_posicion_caballo(tablero, jugador)
        if posicionActual is None:
            return False
        if tablero[fila][columna] not in [8, 9]:
            distanciaFila = abs(fila - posicionActual[0])
            distanciaColumna = abs(columna - posicionActual[1])
            if (distanciaFila == 2 and distanciaColumna == 1) or (distanciaFila == 1 and distanciaColumna == 2):
                return True
            else:
                return False

    def obtener_posicion_caballo(self, tablero, jugador):
        for i in range(len(tablero)):
            for j in range(len(tablero)):
                if jugador == 'Max' and tablero[i][j] == 8:
                    return (i, j)
                if jugador == 'Min' and tablero[i][j] == 9:
                    return (i, j)
        return None

    # arreglar puntaje para que se muestre el verdadero
    def realizarJugada(self, tablero, jugada, jugador):
        fila, columna = jugada[0], jugada[1]
        new = tablero.copy()

        # Borrar la posición anterior del jugador en el nuevo tablero
        jugador_actual = 8 if jugador == 'Max' else 9
        posicion_anterior = np.where(new == jugador_actual)
        new[posicion_anterior] = 0

        if self.casilla_puntos(tablero, fila, columna):
            puntaje = tablero[fila][columna]
            self.sumar_puntaje(jugador, puntaje)
        if jugador == 'Max':
            new[fila, columna] = 8
        elif jugador == 'Min':
            new[fila, columna] = 9
        return new

    def sumar_puntaje(self, jugador, puntuacion):
        if jugador == 'Max':
            self.puntajeMax += puntuacion
        elif jugador == 'Min':
            self.puntajeMin += puntuacion

    def obtener_puntaje(self, jugador):
        if jugador == 'Max':
            return self.puntajeMax
        elif jugador == 'Min':
            return self.puntajeMin

    def oponente(self, jugador):
        if jugador == 'Max':
            return 'Min'
        else:
            return 'Max'

    def hay_puntos_disponibles(self, tablero):
        for fila in tablero:
            for numero in fila:
                if numero in [1, 2, 3, 4, 5, 6, 7]:
                    return True
        return False
        
    def distancia_a_puntos(self, tablero, jugador):
        posicion_jugador = self.obtener_posicion_caballo(tablero, jugador)
        puntos = [1, 2, 3, 4, 5, 6, 7]
        distancia_total = 0

        for fila in range(len(tablero)):
            for columna in range(len(tablero)):
                if tablero[fila][columna] in puntos:
                    posicion_punto = (fila, columna)
                    distancia = math.sqrt((posicion_jugador[0] - posicion_punto[0])**2 + (posicion_jugador[1] - posicion_punto[1])**2)
                    distancia_total += distancia

        return distancia_total

    def evaluar_estado(self, profundidad):
        puntaje_max = self.obtener_puntaje('Max')
        puntaje_min = self.obtener_puntaje('Min')
        factores = [1, 2, 3, 4, 5, 6]
        # movimientos_max = len(self.movimientos_posibles(self.tableroGame, 'Max'))
        # movimientos_min = len(self.movimientos_posibles(self.tableroGame, 'Min'))
        # distancia_a_puntos_max = self.distancia_a_puntos(self.tableroGame, 'Max')
        # distancia_a_puntos_min = self.distancia_a_puntos(self.tableroGame, 'Min')

        # # Penalizar si el movimiento disminuye el puntaje del jugador Max
        # penalizacion_movimiento = 0
        # if puntaje_max < self.puntajeMax:
        #     penalizacion_movimiento = 100

        # Obtener el factor correspondiente a la profundidad actual
        factor = factores[-1] if profundidad > len(factores) else factores[profundidad - 1]

        # # Verificar si hay puntos disponibles para tomar
        # puntaje_disponible = self.hay_puntos_disponibles(self.tableroGame)

        # # Ajustar los factores de evaluación según las condiciones del juego
        # if puntaje_disponible:
        #     # Desequilibrio en el puntaje a favor del jugador Min y puntos disponibles
        #     factor_puntaje = 2
        #     factor_movimientos = 1
        #     factor_distancia = 1
        # else:
        #     # No hay puntos disponibles
        #     factor_puntaje = 1
        #     factor_movimientos = 2
        #     factor_distancia = 2

        return (puntaje_max - puntaje_min) * factor #_puntaje + (movimientos_max - movimientos_min) * factor_movimientos - (distancia_a_puntos_max - distancia_a_puntos_min) * factor_distancia


    def minimax(self, nodo, alfa, beta, movimientos_realizados):
        movimientos_realizados=[]
        if nodo.profundidad == 0 or self.juego_terminado(nodo.tablero):
            print(self.evaluar_estado(nodo.profundidad))
            return self.evaluar_estado(nodo.profundidad)

        if nodo.jugador == 'Max':
            mejorValor = -float("inf")
            movimientos = self.movimientos_posibles(nodo.tablero, nodo.jugador)
            for jugada in movimientos:
                if jugada not in movimientos_realizados:
                    movimientos_realizados.append(jugada)

                    nuevoTablero = self.realizarJugada(nodo.tablero, jugada, nodo.jugador)
                    nuevoNodo = Nodo(nuevoTablero, self.oponente(nodo.jugador), nodo.profundidad - 1)
                    valor = self.minimax(nuevoNodo, alfa, beta, movimientos_realizados)

                    # movimientos_realizados.remove(jugada)
                    print(movimientos_realizados)

                    mejorValor = max(mejorValor, valor)
                    alfa = max(alfa, mejorValor)
                    if alfa >= beta:
                        break

            return mejorValor
        else:
            peorValor = float("inf")
            movimientos = self.movimientos_posibles(nodo.tablero, nodo.jugador)
            for jugada in movimientos:
                if jugada not in movimientos_realizados:
                    movimientos_realizados.append(jugada)
                    nuevoTablero = self.realizarJugada(copy.deepcopy(nodo.tablero), jugada, nodo.jugador)
                    nuevoNodo = Nodo(nuevoTablero, self.oponente(nodo.jugador), nodo.profundidad - 1)
                    valor = self.minimax(nuevoNodo, alfa, beta, movimientos_realizados)
                    peorValor = min(peorValor, valor)
                    beta = min(beta, peorValor)
                    # movimientos_realizados.remove(jugada)
                    if beta <= alfa:
                        break  # Corte alfa-beta
            return peorValor

def verificar_primer_movimiento_max(tablero, profundidad, jugador, movimientos_realizados):
    juego = Juego()
    movimientos_iniciales = juego.movimientos_posibles(tablero, jugador)
    mejor_utilidad = -float('inf')
    alfa = -float("inf")
    beta = float("inf")
    mejor_movimiento = None

    for movimiento in movimientos_iniciales:
        movimientos_realizados.add(movimiento)  # Agregar movimiento al registro
        nuevo_tablero = juego.realizarJugada(copy.deepcopy(tablero), movimiento, jugador)
        nuevo_nodo = Nodo(nuevo_tablero, juego.oponente(jugador), profundidad)
        utilidad = juego.minimax(nuevo_nodo, alfa, beta, movimientos_realizados)
        if utilidad > mejor_utilidad:
            mejor_utilidad = utilidad
            mejor_movimiento = movimiento
        movimientos_realizados.remove(movimiento)  # Eliminar movimiento del registro

    return mejor_movimiento

