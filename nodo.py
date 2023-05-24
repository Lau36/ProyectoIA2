class Nodo:
    def __init__(self, matriz, estadoGanar, tipo, utilidad, puntosMaquina, puntosJugador, alfa, beta, profundidad, nodosVisitados):
        self.matriz = matriz,
        self.estadoGanar = estadoGanar,
        self.tipo = tipo,
        self.utilidad = utilidad,
        self.puntosMaquina = puntosMaquina
        self.puntosJugador = puntosJugador
        self.alfa = alfa,
        self.beta = beta,
        self.nodosVisitados = nodosVisitados,
        self.profundidad = profundidad

    # Funcion que verifica si el agente ya tiene todas las esferas y ha ganado

    def condicionGanar(self):
        if (self.estadoGanar == 1):
            final = "Gana maquina", True
            return final
        if (self.estadoGanar == 0):
            final = "Empate", True
            return final
        else:
            final = "Gana Jugador", True
            return final

    def marcarGanar(self):
        if (self.puntosMaquina > self.puntosJugador):
            self.estadoGanar = 1

        if (self.puntosMaquina < self.puntosJugador):
            self.estadoGanar = -1

        if (self.puntosMaquina == self.puntosJugador):
            self.estadoGanar = 0
