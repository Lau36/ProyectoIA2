from nodo import Nodo
from views.tablero import Tablero
import numpy as np

def generar_tablero():
        tablero = np.zeros((8, 8), dtype=int)

        # Generar una lista de números del 1 al 7 (excluyendo el 8 y 9)
        numeros = list(range(1, 8))

        imagenes_caballos = ["resources/images/caballo_blanco.png", "resources/images/caballo_negro.png"]

        # Asignar los números en posiciones aleatorias del tablero sin superposición
        for num in numeros:
            while True:
                posicion = np.random.randint(8*8)
                fila, columna = np.unravel_index(posicion, (8, 8))
                if tablero[fila, columna] == 0:
                    tablero[fila, columna] = num
                    break

        # Asignar el número 8 en una posición aleatoria para representar el caballo blanco
        while True:
            posicion = np.random.randint(8*8)
            fila, columna = np.unravel_index(posicion, (8, 8))
            if tablero[fila, columna] == 0:
                tablero[fila, columna] = 8
                posicion_caballoB =(columna, fila)
                break

        # Asignar el número 9 en una posición aleatoria para representar el caballo negro
        while True:
            posicion = np.random.randint(8*8)
            fila, columna = np.unravel_index(posicion, (8, 8))
            if tablero[fila, columna] == 0:
                tablero[fila, columna] = 9
                posicion_caballoN = (columna, fila)
                break

        return tablero, posicion_caballoB, posicion_caballoN, imagenes_caballos

def obtener_movimientos_caballo(posicion_caballo):
        movimientos = []
        offsets = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        
        for offset in offsets:
            nueva_columna = posicion_caballo[0] + offset[0]
            nueva_fila = posicion_caballo[1] + offset[1]
            
            if 0 <= nueva_columna < 8 and 0 <= nueva_fila < 8:
                movimientos.append((nueva_columna, nueva_fila))
        
        return movimientos

tablero, posicion_caballoB, posicion_caballoN = generar_tablero()
posibles = obtener_movimientos_caballo(posicion_caballoB)
print(tablero)
print (posicion_caballoB)
print(posibles)

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
