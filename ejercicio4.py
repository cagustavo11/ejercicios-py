"""
4. Pedir números hasta que se teclee uno negativo, y mostrar cuántos números se han introducido.
"""
numbers = 0
while True:
    number = int(input('Ingrese un número: '))
    if number < 0:
        break
    numbers += 1
print(f'Se han introducido: {numbers} números en total')
