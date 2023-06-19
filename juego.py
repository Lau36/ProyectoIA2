import numpy as np

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

    def realizarJugada(self, tablero, jugada, jugador):
        fila, columna = jugada[0], jugada[1]
        new = tablero.copy()
        if self.casilla_puntos(tablero, fila, columna):
            puntaje = tablero[fila][columna]
            self.sumar_puntaje(jugador, puntaje)
            print("El puntaje que lleva es:", self.sumar_puntaje(jugador, puntaje))
        if jugador == 'Max':
            new[fila, columna] = 8
        elif jugador == 'Min':
            new[fila, columna] = 9
        return new

    def sumar_puntaje(self, jugador, puntuacion):
        if jugador == 'Max':
            self.puntajeMax += puntuacion
            return self.puntajeMax
        elif jugador == 'Min':
            self.puntajeMin += puntuacion
            return self.puntajeMin

    def oponente(self, jugador):
        if jugador == 'Max':
            return 'Min'
        else:
            return 'Max'

    def evaluar_estado(self):
        utilidad = self.puntajeMax - self.puntajeMin
        return utilidad
    

# Instancia clase Juego
juego = Juego()
# LLamar a los métodos de la clase
tablero, posicionJugadorMax, posicionJugadorMin = juego.obtener_tablero()
jugadas_posiblesMax = juego.movimientos_posibles(tablero, 'Max')
jugadas_posiblesMin = juego.movimientos_posibles(tablero, 'Min')
obtenerTablero = juego.obtener_tablero(reset=True)
print(tablero)
print(obtenerTablero)
print(posicionJugadorMax)
print(posicionJugadorMin)
print(jugadas_posiblesMax)
print(jugadas_posiblesMin)