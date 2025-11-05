print('Dame el numero de chicos de la clase')
chicos = int(input())
print('Dame el numero de chicas de la clase')
chicas = int(input())

total = chicos + chicas
pchicas=(chicas/total)*100
pchicos=(chicos/total)*100

print('RESUMEN')
print(f'El numero total de alumnos es {total}')

print(f'El porcentaje de las chicas es de {pchicas:.2f}%')
print(f'El porcentaje de las chicos es de {pchicos:.2f}%')