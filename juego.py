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
        
    #mejorar utilidad multiplicar puntaje si es cercano a las primeras jugadas
    def evaluar_estado(self):
        utilidad = self.puntajeMax - self.puntajeMin
        return utilidad
    
class Nodo:
    def __init__(self, tablero, jugador, profundidad):
        self.tablero = tablero
        self.jugador = jugador
        self.profundidad = profundidad

    def obtener_utilidad(self):
        # Implementa aquí la lógica para obtener la utilidad del nodo
        
        utilidad = 0
        return utilidad
    

def minimax(nodo, juego, alfa, beta):
    if nodo.profundidad == 0 or juego.juego_terminado(nodo.tablero):
        return nodo.obtener_utilidad()

    if nodo.jugador == 'Max':
        mejorValor = float("-inf")
        movimientos = juego.movimientos_posibles(nodo.tablero, nodo.jugador)
        for jugada in movimientos:
            nuevoTablero = juego.realizarJugada(
                nodo.tablero, jugada, nodo.jugador)
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
            nuevoTablero = juego.realizarJugada(
                nodo.tablero, jugada, nodo.jugador)
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

if __name__ == "__main__":
    juego = Juego()
    juego.generar_tablero()
    profundidad = juego.complejidad_juego('principiante')
    jugador = 'Min'

    while True:
        print("Tablero actual:")
        print(juego.tableroGame)
        print("Turno del jugador 'Min'. Ingresa las coordenadas de la jugada (fila y columna separadas por espacios):")
        fila, columna = map(int, input().split())
        jugada_min = (fila, columna)

        if juego.alcanzar_casilla(juego.tableroGame, jugador, fila, columna):
            nuevo_tablero = juego.realizarJugada(juego.tableroGame, jugada_min, jugador)
            print("Jugada del jugador 'Min':", jugada_min)
            print("Nuevo tablero:")
            print(nuevo_tablero)

            if juego.juego_terminado(nuevo_tablero):
                print("El juego ha terminado. ¡Ganó el jugador 'Min'!")
                break

            mejor_movimiento_max = verificar_primer_movimiento_max(nuevo_tablero, profundidad, 'Max')
            nuevo_tablero = juego.realizarJugada(nuevo_tablero, mejor_movimiento_max, 'Max')
            print("Jugada del jugador 'Max':", mejor_movimiento_max)
            print("Nuevo tablero:")
            print(nuevo_tablero)

            if juego.juego_terminado(nuevo_tablero):
                print("El juego ha terminado. ¡Ganó el jugador 'Max'!")
                break

            juego.tableroGame = nuevo_tablero
        else:
            print("La jugada ingresada no es válida. Inténtalo de nuevo.")

    print(juego.tableroGame)
    print("jugada", verificar_primer_movimiento_max(juego.tableroGame, 4, jugador))