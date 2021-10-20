"""
1. Leer un número y mostrar su cuadrado, repetir el proceso hasta que se introduzca un número negativo.
"""


while True:
    number = int(input('introduce un número: '))
    if number < 0:
        break
    print(f'el cuadrado de su número es: {number ** 2}')
