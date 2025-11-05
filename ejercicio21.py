import random
import time

print("¡Bienvenido al juego de Adivinar un Número!")
print("Tienes que adivinar un número entre 1 y 100.")

numero_secreto = random.randint(1, 100)
tiempo_inicio = time.time()
intentos = 0
adivinado = False

while not adivinado:
    try:
        adivinanza = int(input("Introduce tu adivinanza: "))
        intentos += 1

        if adivinanza == numero_secreto:
            adivinado = True
            print(f"¡Felicidades! Adivinaste el número {numero_secreto}.")
        elif adivinanza < numero_secreto:
            print("El número secreto es MAYOR.")
        else:
            print("El número secreto es MENOR.")

        time.sleep(0.5)

    except ValueError:
        print("¡Error! Por favor, introduce solo números enteros.")

tiempo_final = time.time()
duracion = tiempo_final - tiempo_inicio

print("-" * 30)
print(f"Número de intentos: {intentos}")
print(f"Duración del juego: {duracion:.2f} segundos")
print("¡Gracias por jugar!")