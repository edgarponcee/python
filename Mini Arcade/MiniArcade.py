import random
import time
import sys

DIFICULTADES = {
    '1': (20, 5, "Fácil (1-20, 5 intentos)"),
    '2': (50, 7, "Normal (1-50, 7 intentos)"),
    '3': (100, 10, "Difícil (1-100, 10 intentos)")
}

def ascii_header():
    print("""
  ╔═══════════════════════════════════╗
  ║    LABORATORIO MINI-ARCADE    ║
  ║  ¡Elige tu aventura en la consola! ║
  ╚═══════════════════════════════════╝""")

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Piedra, Papel o Tijera (vs Bot)")
    print("2. Adivina el Número (con dificultad y tiempo)")
    print("3. Cálculo Mental (límite 30s)")
    print("4. Eco Loco (Análisis de texto)")
    print("0. Salir de la Arcade")
    print("----------------------")

def juego_ppt():
    opciones = {'P': 'Piedra', 'L': 'Papel', 'T': 'Tijera'}
    print("\n[JUEGO: Piedra, Papel o Tijera]")
    print("Opciones: P (Piedra), L (Papel), T (Tijera). Escribe '0' para volver al menú.")
    
    while True:
        try:
            u = input("Tu elección (P/L/T o 0): ").strip().upper()
            if u == '0': return
            if u not in opciones:
                print("Opción inválida. Usa P, L, T, o 0.")
                continue

            b = random.choice(list(opciones.keys()))
            print(f"Bot eligió: {opciones[b]}\nTú elegiste: {opciones[u]}")

            if u == b: print("¡Empate!")
            elif (u == 'P' and b == 'T') or (u == 'L' and b == 'P') or (u == 'T' and b == 'L'):
                print("¡Ganaste esta ronda!")
            else:
                print("¡Perdiste! El Bot gana.")
        except:
            print("Error de entrada. Inténtalo de nuevo.")

def juego_adivina_numero():
    print("\n[JUEGO: Adivina el Número]")
    print("--- Elige Dificultad ---\n1. Fácil (1-20, 5 intentos)\n2. Normal (1-50, 7 intentos)\n3. Difícil (1-100, 10 intentos)\n0. Volver")

    while True:
        op = input("Elige (1/2/3 o 0): ").strip()
        if op == '0': return
        if op in DIFICULTADES:
            MAX_NUM, MAX_INTENTOS, NOMBRE_DIF = DIFICULTADES[op]
            break
        print("Opción de dificultad inválida.")
    
    secreto = random.randint(1, MAX_NUM)
    intentos = 0
    print(f"\n¡Adivina el número entre 1 y {MAX_NUM}! Tienes {MAX_INTENTOS} intentos.")
    input("Presiona ENTER para empezar a contar el tiempo...")
    inicio = time.time() 

    while intentos < MAX_INTENTOS:
        try:
            intento = int(input(f"Intento {intentos + 1}/{MAX_INTENTOS}. Tu número: "))
            intentos += 1

            if not (1 <= intento <= MAX_NUM):
                print(f"El número debe estar entre 1 y {MAX_NUM}.")
                continue

            if intento == secreto:
                total = round(time.time() - inicio, 2)
                puntuacion = max(10, int(1000 - (intentos - 1) * 50 - total * 10))
                
                print(f"\n¡FELICIDADES! ¡Adivinaste el número {secreto}!")
                print(f"Estadísticas: {intentos} intentos en {total} segundos.")
                print(f"Tu Puntuación en dificultad '{NOMBRE_DIF}': {puntuacion} puntos.")
                return

            print("¡Sube! El número secreto es mayor." if intento < secreto else "¡Baja! El número secreto es menor.")
            time.sleep(0.5)

        except ValueError:
            print("Entrada inválida. Por favor, introduce un número entero.")
        except:
            print("Error inesperado. Reiniciando juego.")
            return

    print(f"\nGame Over. Te quedaste sin intentos. El número secreto era: {secreto}.")

def juego_calculo_mental():
    print("\n[JUEGO: Cálculo Mental]")
    print("Resuelve tantas operaciones como puedas. ¡Tienes 30 segundos!")
    input("Presiona ENTER para comenzar...")

    puntuacion, limite, ops = 0, 30, ['+', '-', '*']
    inicio = time.time()

    while (time.time() - inicio) < limite:
        try:
            n1, n2, op = random.randint(5, 20), random.randint(1, 15), random.choice(ops)
            if op == '-' and n1 < n2: n1, n2 = n2, n1

            problema = f"{n1} {op} {n2}"
            correcta = eval(problema)
            restante = int(limite - (time.time() - inicio))
            
            if restante <= 0: break
                
            pregunta = input(f"\n[Tiempo restante: {restante}s] ¿Cuánto es {problema}?: ")
            if (time.time() - inicio) >= limite:
                print("\n¡TIEMPO AGOTADO!")
                break

            usuario = int(pregunta.strip())

            if usuario == correcta:
                puntuacion += 1
                print("¡Correcto!")
            else:
                print(f"Incorrecto. La respuesta era {correcta}.")
                
        except ValueError:
            print("Entrada inválida. Introduce un número.")
        except Exception as e:
            print(f"Error interno del juego.")
            break

    total_final = round(time.time() - inicio, 2)
    print(f"\n--- FIN DEL JUEGO ---\nHas respondido {puntuacion} preguntas correctamente en {total_final} segundos.")

def juego_eco_loco():
    print("\n[JUEGO: Eco Loco - Análisis de Texto]")
    print("Introduce una frase o palabra. Escribe '0' para volver al menú.")
    
    while True:
        try:
            t = input("Tu texto: ").strip()

            if t == '0': return
            if not t:
                print("No has introducido nada. Inténtalo de nuevo.")
                continue

            inv = t[::-1]
            caracteres = len(t)
            vocales_set = 'aeiouáéíóúAEIOUÁÉÍÓÚ'
            vocales = sum(1 for char in t if char in vocales_set)

            print("\n--- Resultados del Eco ---")
            print(f"Original: '{t}'")
            print(f"Invertida: '{inv}'")
            print(f"Nº de Caracteres: {caracteres}")
            print(f"Nº de Vocales: {vocales}")
            print("--------------------------")

        except:
            print("Error de procesamiento. Intenta con un texto diferente.")

def main():
    ascii_header()
    
    while True:
        mostrar_menu()
        
        op = ""
        while op not in ['0', '1', '2', '3', '4']:
            op = input("Elige una opción (0-4): ").strip()
            if op not in ['0', '1', '2', '3', '4']:
                print("Opción inválida. Introduce un número del 0 al 4.")
        
        if op == '0':
            print("\n¡Gracias por jugar en el Laboratorio de Juegos Retro del Insti!")
            print("Hasta la próxima.")
            sys.exit(0)
        elif op == '1': juego_ppt()
        elif op == '2': juego_adivina_numero()
        elif op == '3': juego_calculo_mental()
        elif op == '4': juego_eco_loco()
        
        if op != '0':
            input("\n[Presiona ENTER para volver al menú principal...]")

if __name__ == "__main__":
    main()