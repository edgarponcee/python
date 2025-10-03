# Factura.py

total = 0

precio = float(input("Introduce un precio (0 para terminar): "))

while precio != 0:
    total += precio
    precio = float(input("Introduce un precio (0 para terminar): "))

print(f"Total de la factura: {total:.2f}")
