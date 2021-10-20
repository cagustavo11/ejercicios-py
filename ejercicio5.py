"""
5. Realizar un juego para adivinar un número. Para ello generar un número aleatorio entre 0-100, y luego ir pidiendo números indicando “es mayor” o “es menor” según sea mayor o menor con respecto a N. El proceso termina cuando el usuario acierta y mostrar el número de intentos.
"""
import random

# La función randint() del packete random nos sirve para generar números aleatorios
numero_aleatorio = random.randint(0, 100)

numero_intentos = 0
while True:
    user_num = int(input('Ingrese un número: '))

    if numero_aleatorio > user_num:
        print('es mayor')
    if numero_aleatorio < user_num:
        print('es menor')
    if user_num == numero_aleatorio:
        break
    numero_intentos += 1

print('--------')
print(f'¡Acertaste!')
print(f'El número de intentos es: {numero_intentos}')
