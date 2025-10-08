total_bruto = 0
descuento_total = 0
iva_porcentaje = 0.10
cont_baratas = 0
cont_medias = 0
cont_caras = 0
precio_minimo = float('inf')
precio_maximo = float('-inf')

while True:
    try:
        N = int(input("¿Cuántas líneas tendrá la factura (1-50)? "))
        if 1 <= N <= 50:
            break
        else:
            print("Error: 1 a 50.")
    except ValueError:
        print("Error: Número entero.")

for i in range(1, N + 1):
    print(f"\n--- Línea {i} de {N} ---")
    
    while True:
        try:
            precio = float(input("Introduce el precio (>= 0): "))
            if precio >= 0:
                break
            else:
                print("Error: Precio no negativo.")
        except ValueError:
            print("Error: Número válido para el precio.")

    while True:
        try:
            cantidad = int(input("Introduce la cantidad (>= 1): "))
            if cantidad >= 1:
                break
            else:
                print("Error: Cantidad >= 1.")
        except ValueError:
            print("Error: Número entero para la cantidad.")

    subtotal_linea = precio * cantidad
    total_bruto += subtotal_linea

    if precio < precio_minimo:
        precio_minimo = precio
    if precio > precio_maximo:
        precio_maximo = precio

    if precio < 5:
        cont_baratas += 1
    elif 5 <= precio <= 20:
        cont_medias += 1
    else:
        cont_caras += 1
    
porcentaje_descuento = 0

if total_bruto >= 100:
    porcentaje_descuento = 0.15
elif total_bruto >= 50:
    porcentaje_descuento = 0.10
elif total_bruto >= 20:
    porcentaje_descuento = 0.05
else:
    porcentaje_descuento = 0.00

descuento_aplicado = total_bruto * porcentaje_descuento
base_imponible = total_bruto - descuento_aplicado

iva_calculado = base_imponible * iva_porcentaje
total_factura = base_imponible + iva_calculado

print("\n" + "="*40)
print("             RESUMEN DE FACTURA")
print("="*40)

print(f"Total bruto: {total_bruto:,.2f} €")
print(f"Descuento ({porcentaje_descuento*100:.0f}%): {descuento_aplicado:,.2f} €")
print("-" * 40)
print(f"Base Imponible: {base_imponible:,.2f} €")
print(f"IVA (10%): {iva_calculado:,.2f} €")
print("-" * 40)
print(f"TOTAL A PAGAR: {total_factura:,.2f} €")

print("\n" + "="*40)
print("             RESUMEN DE LÍNEAS")
print("="*40)

print(f"Líneas baratas: {cont_baratas}")
print(f"Líneas medias: {cont_medias}")
print(f"Líneas caras: {cont_caras}")

if N > 0:
    print(f"\nPrecio mínimo: {precio_minimo:,.2f} €")
    print(f"Precio máximo: {precio_maximo:,.2f} €")
else:
    print("\nNo hay líneas.")

print("="*40)