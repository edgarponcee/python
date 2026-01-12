class equipo:
    def __init__(self, nom_eq):
        self.nombre_equipo = nom_eq
        self.jugadores_eq = []

    def anyadir_jugador(self, jugador):
        self.jugadores_eq.append(jugador)


class jugador:
    # constructor
    def __init__(self, dor, nom, eq):
        self.dorsal = dor
        self.nombre = nom
        self.equipo = eq

    def mostrar(self):
        print(f"{self.dorsal}.{self.nombre}")

    def anyadir_equipo(self, equipo):
        self.equipo = equipo
        equipo.anyadir_jugador(self)


# Programa Principal
equipo1 = equipo("FC Barcelona")
equipo2 = equipo("Real Madrid")

jugador1 = jugador(11, "Raphinha", equipo1)
jugador2 = jugador(7, "Vinicius", equipo2)
jugador3 = jugador(23, "Mijatovic", equipo2)
jugador4 = jugador(12, "Marcelo", equipo2)

jugador1.anyadir_equipo(equipo1)
jugador2.anyadir_equipo(equipo2)
jugador3.anyadir_equipo(equipo2)
jugador4.anyadir_equipo(equipo2)

print(f"Jugadores del {equipo2.nombre_equipo}:")
for jugador in equipo2.jugadores_eq:
    jugador.mostrar()