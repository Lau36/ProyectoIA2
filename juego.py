import numpy as np
from nodo import Nodo

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
        for fila in range(8):
            for columna in range(8):
                if self.alcanzar_casilla(tablero, jugador, fila, columna):
                    jugada = (fila, columna)
                    jugadas_posibles.append(jugada)
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
            print("FUN OBT puntaje max",self.puntajeMax)
            return self.puntajeMax
        elif jugador == 'Min':
            print("FUN OBT puntaje min",self.puntajeMin)
            return self.puntajeMin

    def oponente(self, jugador):
        if jugador == 'Max':
            return 'Min'
        else:
            return 'Max'
        
    #mejorar utilidad multiplicar puntaje si es cercano a las primeras jugadas
    def evaluar_estado(self):
        puntaje_max = self.obtener_puntaje('Max')
        puntaje_min = self.obtener_puntaje('Min')
        puntos_disponibles = 0
        
        for fila in self.tableroGame:
            for numero in fila:
                if numero in range(1, 8):
                    puntos_disponibles += 1
        
        if puntaje_max == 0 and puntaje_min == 0:
            return 0  # Ambos jugadores tienen puntaje 0, se considera empate
        
        if puntaje_max == puntos_disponibles:
            return float('inf')  # 'Max' ha recolectado todos los puntos
    
        return puntaje_max - puntaje_min
    
def minimax(nodo, juego, alfa, beta):
    if nodo.profundidad == 0 or juego.juego_terminado(nodo.tablero):
        return juego.evaluar_estado()

    if nodo.jugador == 'Max':
        mejorValor = float("-inf")
        movimientos = juego.movimientos_posibles(nodo.tablero, nodo.jugador)
        for jugada in movimientos:
            nuevoTablero = juego.realizarJugada(nodo.tablero, jugada, nodo.jugador)
            nuevoNodo = Nodo(nuevoTablero, juego.oponente(nodo.jugador), nodo.profundidad - 1)
            valor = minimax(nuevoNodo, juego, alfa, beta)
            mejorValor = max(mejorValor, valor)
            alfa = max(alfa, mejorValor)
            if beta <= alfa:
                break  # Poda alfa-beta
        return mejorValor

    else:
        mejorValor = float("inf")
        movimientos = juego.movimientos_posibles(nodo.tablero, nodo.jugador)
        for jugada in movimientos:
            nuevoTablero = juego.realizarJugada(nodo.tablero, jugada, nodo.jugador)
            nuevoNodo = Nodo(nuevoTablero, juego.oponente(nodo.jugador), nodo.profundidad - 1)
            valor = minimax(nuevoNodo, juego, alfa, beta)
            mejorValor = min(mejorValor, valor)
            beta = min(beta, mejorValor)
            if beta <= alfa:
                break  # Poda alfa-beta
        return mejorValor

def verificar_primer_movimiento_max(tablero, profundidad, jugador):
    juego = Juego()
    movimientos_iniciales = juego.movimientos_posibles(tablero, jugador)
    mejor_utilidad = float('-inf')
    alfa = float("-inf")
    beta = float("inf")
    mejor_movimiento = None

    for movimiento in movimientos_iniciales:
        nuevo_tablero = juego.realizarJugada(tablero, movimiento, jugador)
        nuevo_nodo = Nodo(nuevo_tablero, juego.oponente(jugador), profundidad)
        utilidad = minimax(nuevo_nodo, juego, alfa, beta)
        if utilidad > mejor_utilidad:
            mejor_utilidad = utilidad
            mejor_movimiento = movimiento

    return mejor_movimiento