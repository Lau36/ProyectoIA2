from nodo import Nodo


def profundidad(matriz_juego):
    nodos_creados = 0
    nodos_expandidos = 0
    pos_esfera = []

    raiz = Nodo(
    )

    pila = [raiz]

    while len(pila) > 0:
        nodo = pila.pop()
        nodos_expandidos += 1
        if (nodo.condicionGanar[1]):
            ganador = nodo.condicionGanar[0]
            return ganador, nodo.puntosMaquina, nodo.puntosJugador

        else:
            return "Continuara..."

        # genero los hijos

    return "No hay solucion", matriz_juego
