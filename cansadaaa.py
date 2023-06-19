import random

TAM_TABLERO = 8
NUM_CASILLAS_PUNTOS = 7

casillas_puntos = random.sample([(i, j) for i in range(TAM_TABLERO) for j in range(TAM_TABLERO)], NUM_CASILLAS_PUNTOS)

def generar_estado_inicial():
    # Generar un estado inicial aleatorio del juego
    estado = {
        'tablero': [[0] * TAM_TABLERO for _ in range(TAM_TABLERO)],
        'turno': 'maquina'
    }
    return estado

def obtener_movimientos_legales(estado):
    # Obtener los movimientos legales disponibles en un estado dado
    # Por ejemplo, obtener las casillas vacías en el tablero
    movimientos = []
    for i in range(TAM_TABLERO):
        for j in range(TAM_TABLERO):
            if estado['tablero'][i][j] == 0:
                movimientos.append((i, j))
    return movimientos

def evaluar_estado(estado):
    # Evaluar un estado del juego y asignarle un valor de utilidad
    # Por ejemplo, sumar los puntos de cada jugador
    puntaje_maquina = sum(estado['tablero'][i][j] for i, j in casillas_puntos)
    puntaje_jugador = sum(estado['tablero'][i][j] for i, j in casillas_puntos)
    return puntaje_maquina - puntaje_jugador

def estado_terminado(estado):
    # Verificar si el estado del juego indica que este ha terminado
    # Por ejemplo, si no hay más movimientos legales
    return len(obtener_movimientos_legales(estado)) == 0

def realizar_movimiento(estado, movimiento):
    # Realizar un movimiento en el estado del juego y retornar el nuevo estado resultante
    nuevo_estado = estado.copy()
    i, j = movimiento
    nuevo_estado['tablero'][i][j] = 1 if estado['turno'] == 'maquina' else -1
    nuevo_estado['turno'] = 'jugador' if estado['turno'] == 'maquina' else 'maquina'
    return nuevo_estado

def turno_maquina(estado):
    # Verificar si es el turno de la máquina
    return estado['turno'] == 'maquina'

def obtener_movimiento_jugador():
    # Obtener el movimiento seleccionado por el jugador
    movimiento = input("Selecciona una casilla en formato fila, columna (por ejemplo, 2,3): ")
    fila, columna = movimiento.split(',')
    return int(fila), int(columna)

def tomar_decision_imperfecta():
    return random.random() < 0.8  # Probabilidad del 80% de tomar la decisión óptima

def minimax(estado, profundidad, es_maximizando):
    if profundidad == 0 or estado_terminado(estado):
        return evaluar_estado(estado)
    
    mejor_valor = float('-inf') if es_maximizando else float('inf')
    movimientos_legales = obtener_movimientos_legales(estado)
    
    for movimiento in movimientos_legales:
        nuevo_estado = realizar_movimiento(estado, movimiento)
        valor = minimax(nuevo_estado, profundidad - 1, not es_maximizando)
        
        if es_maximizando:
            if tomar_decision_imperfecta():
                mejor_valor = max(mejor_valor, valor)
            else:
                return mejor_valor
        else:
            if tomar_decision_imperfecta():
                mejor_valor = min(mejor_valor, valor)
            else:
                return mejor_valor
    
    return mejor_valor

def jugar():
    estado_actual = generar_estado_inicial()
    
    while not estado_terminado(estado_actual):
        if turno_maquina(estado_actual):
            mejor_movimiento = None
            mejor_valor = float('-inf')
            
            movimientos_legales = obtener_movimientos_legales(estado_actual)
            
            for movimiento in movimientos_legales:
                nuevo_estado = realizar_movimiento(estado_actual, movimiento)
                valor = minimax(nuevo_estado, profundidad_limite, False)
                
                if valor > mejor_valor:
                    mejor_valor = valor
                    mejor_movimiento = movimiento
            
            estado_actual = realizar_movimiento(estado_actual, mejor_movimiento)
        else:
            movimiento_jugador = obtener_movimiento_jugador()
            estado_actual = realizar_movimiento(estado_actual, movimiento_jugador)
    
    # Mostrar resultado del juego
    resultado = evaluar_estado(estado_actual)
    if resultado > 0:
        print("¡Gana la máquina!")
    elif resultado < 0:
        print("¡Gana el jugador!")
    else:
        print("¡Empate!")

# Ejecutar el juego
profundidad_limite = 3  # Profundidad límite del árbol minimax
jugar()