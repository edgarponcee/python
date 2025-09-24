
n1 = float(input("Escribe la primera nota (0-10): "))
n2 = float(input("Escribe la segunda nota (0-10): "))
n3 = float(input("Escribe la tercera nota (0-10): "))

if n1 <= 4 and n2 <= 4 and n3 <= 4:
    nota_final = 0
elif (n1 > 4 or n2 > 4 or n3 > 4) and not (n1 > 4 and n2 > 4 and n3 > 4):
    nota_final = 2
else:
    nota_final = (0.3 * n1) + (0.2 * n2) + (0.5 * n3)

print("La nota final es:", round(nota_final, 2))
print("Fin del programa")
