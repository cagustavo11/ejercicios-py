"""
20. Pedir 10 números, y mostrar al final si se ha introducido alguno negativo.
"""

negativos = 0

for i in range(10):
    num = int(input('ingrese un número: '))

    if num < 0:
        negativos += 1

print(f'Se han introducido {negativos} números negativos')
