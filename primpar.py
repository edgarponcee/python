def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def esPrimo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

print("Ejecución del Programa Principal")

num1 = 20
num2 = 12
resultado_mcd = mcd(num1, num2)

print(f"El Máximo Común Divisor de {num1} y {num2} es: {resultado_mcd}")

print("Los números primos del 1 al 50 son:")

primos_encontrados = []
for n in range(1, 51):
    if esPrimo(n):
        primos_encontrados.append(n)

print(primos_encontrados)

print("\nAnálisis de Par/Impar de los números primos:")
for primo in primos_encontrados:
    if primo % 2 == 0:
        print(f"El número {primo} es par.")
    else:
        print(f"El número {primo} es impar.")