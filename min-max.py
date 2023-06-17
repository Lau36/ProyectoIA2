from nodo import Nodo

import numpy as np

def generar_tablero():
    tablero = np.zeros((8, 8), dtype=int)

    # Generar una lista de números del 1 al 9
    numeros = list(range(1, 10))

    # Asignar los números en posiciones aleatorias del tablero sin superposición
    for num in numeros:
        while True:
            posicion = np.random.randint(8*8)
            fila, columna = np.unravel_index(posicion, (8, 8))
            if tablero[fila, columna] == 0:
                tablero[fila, columna] = num
                if num == 8:
                    # posicion_caballoB =(columna,fila)
                    columna_caballoB = columna
                    fila_caballoB = fila
                elif num == 9:
                    posicion_caballoN =(columna,fila)
                break
    resultados = tablero,columna_caballoB,fila_caballoB,posicion_caballoN            
    return resultados


def obtener_movimientos_caballo(tablero, fila, columna):
    movimientos = []
    
    movimientos_potenciales = [(fila + 2, columna + 1), (fila + 2, columna - 1),
                              (fila - 2, columna + 1), (fila - 2, columna - 1),
                              (fila + 1, columna + 2), (fila + 1, columna - 2),
                              (fila - 1, columna + 2), (fila - 1, columna - 2)]
    
    for movimiento in movimientos_potenciales:
        nueva_fila, nueva_columna = movimiento
        if 0 <= nueva_fila < 8 and 0 <= nueva_columna < 8: # No salirse del tablero
            if tablero[nueva_fila][nueva_columna] not in [8, 9]: # No es un caballo
                movimientos.append(movimiento)
    
    return movimientos

tablero, columna_caballoB, fila_caballoB,posicion_caballoN = generar_tablero()
print(tablero,columna_caballoB,fila_caballoB,posicion_caballoN )

# Mover el caballo negro
movimientos = obtener_movimientos_caballo(tablero,fila_caballoB, columna_caballoB)
print(movimientos)

# # print("Tablero inicial:")
# print(generar_tablero())
# print(generar_tablero()[1],generar_tablero()[2])
# # Mover el caballo negro
# movimientos = obtener_movimientos_caballo(generar_tablero()[1],generar_tablero()[2])
# print(movimientos)
# if movimientos:
#     nuevo_movimiento = np.random.choice(len(movimientos))
#     nueva_fila, nueva_columna = movimientos[nuevo_movimiento]
#     tablero[fila_8, columna_8] = 0  # Limpiar la posición anterior
#     tablero[nueva_fila, nueva_columna] = 9  # Mover el caballo negro
#     print("Tablero después del movimiento del caballo negro:")
#     print(tablero)
# else:
#     print("No hay movimientos válidos para el caballo negro.")

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
