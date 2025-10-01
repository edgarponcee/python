# Número secreto
secreto = 9

print("Adivina el número secreto (entre 1 y 10")

numero = 0
while numero != secreto:
    numero = int(input("Introduce un número:"))

    if numero == secreto:
        print("Correcto!")
    else:
        if numero > secreto:
            print("Muy alto")
        else:
            print("Muy bajo")
