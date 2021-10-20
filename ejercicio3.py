"""
3. Leer números hasta que se introduzca un 0. Para cada uno indicar si es par o impar
"""

while True:
    num = int(input('introduzca un número: '))
    print('-------------')
    if num % 2 == 0:
        print('Es un número par')
    if num % 2 != 0:
        print('Es un número impar')

    if num == 0:
        break
