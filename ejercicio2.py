"""
2. Leer un número e indicar si es positivo o negativo. El proceso se repetirá hasta que se introduzca un 0.
"""
while True:
    num = int(input('introduzca un número: '))
    print('-------------')
    if num > 0:
        print('Es un número positivo')

    if num < 0:
        print('Es un número negativo')

    if num == 0:
        break
