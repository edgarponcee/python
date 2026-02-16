class Jugador:
    def __init__(self, d, n):
        self.dorsal = d
        self.nombre = n

    def mostrar(self):
        # Formato dorsal.nombre (ej: 16.PauGasol)
        print(f"{self.dorsal}.{self.nombre}")

# Uso en el programa principal
p1 = Jugador(16, "PauGasol")
p1.mostrar()