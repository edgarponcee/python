saldo = 1000

while True:
    print("Tu saldo es:", saldo)
    monto = int(input("Introduce el monto a retirar (0 para salir): "))

    if monto == 0:
        print("Gracias por usar el cajero.")
        break
    elif monto <= 0:
        print("Monto no válido")
    elif monto > saldo:
        print("Saldo insuficiente")
    elif monto % 10 != 0:
        print("El monto debe ser múltiplo de 10")
    else:
        saldo -= monto
        print("Has retirado", monto, "euros.")

