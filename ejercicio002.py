class Equipo:
    def __init__(self, nombre_equipo):
        self.nombre = nombre_equipo

class Jugador:
    def __init__(self, d, n, equipo_objeto):
        self.dorsal = d
        self.nombre = n
        self.equipo = equipo_objeto # Aquí guardamos el objeto equipo

    def mostrar_todo(self):
        print(f"{self.nombre} juega en el {self.equipo.nombre}")

# 1. Creamos el equipo
mi_equipo = Equipo("Lakers")
# 2. Creamos el jugador y le pasamos ese equipo
p1 = Jugador(16, "Pau Gasol", mi_equipo)
p1.mostrar_todo()