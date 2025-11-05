# SumaSecuencia.py

secuencia = input("Introduce números separados por espacios: ")
numeros_texto = secuencia.split()
suma_total = 0

for texto in numeros_texto:
    try:
        numero = float(texto)
        suma_total = suma_total + numero
    except ValueError:
        pass  # Ignorar si no es un número

print(f"La suma es: {suma_total}") 