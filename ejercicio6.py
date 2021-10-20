"""
6. Pedir números hasta que se teclee un 0, mostrar la suma de todos los números, introducidos.
"""

acumular_suma = 0
while True:
    num = int(input('introduzca un número: '))
    if num == 0:
        break
    acumular_suma += num

print(f'La suma de todos los números introducidos es: {acumular_suma}')
