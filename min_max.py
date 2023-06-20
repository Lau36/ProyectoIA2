from juego import Juego
from nodo import Nodo

def minimax(nodo, juego, alfa, beta):
    if (nodo, 'profundidad') and (nodo.profundidad == 0 or juego.juego_terminado(nodo.tablero)):
        return nodo.obtener_utilidad()

    if (nodo.jugador == 'Max'):
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
    jugador = 'Max'  # Cambia 'Min' a 'Max'

    while True:
        print("Tablero actual:")
        print(juego.tableroGame)

        if jugador == 'Min':
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

                juego.tableroGame = nuevo_tablero
        else:
            mejor_movimiento_max = verificar_primer_movimiento_max(juego.tableroGame, profundidad, 'Max')
            nuevo_tablero = juego.realizarJugada(juego.tableroGame, mejor_movimiento_max, 'Max')
            print("Jugada del jugador 'Max':", mejor_movimiento_max)
            print("Nuevo tablero:")
            print(nuevo_tablero)

            if juego.juego_terminado(nuevo_tablero):
                print("El juego ha terminado. ¡Ganó el jugador 'Max'!")
                break

            juego.tableroGame = nuevo_tablero

        # Cambiar el turno del jugador
        jugador = 'Min' if jugador == 'Max' else 'Max'

    print(juego.tableroGame)
    print("jugada", verificar_primer_movimiento_max(juego.tableroGame, 4, jugador))


if __name__ == "__main__":
    juego = Juego()