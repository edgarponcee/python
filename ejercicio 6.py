print("Introduce tu edad")
edad = int(input())

if edad < 0 or edad > 120:
    print("Edad no válida")
elif edad < 18:
    print("El alumno es menor de edad")
else:
    print("Es alumno es mayor de edad")