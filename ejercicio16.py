"""
16. Pide un número (que debe estar entre 0 y 10) y mostrar la tabla de multiplicar de dicho número
"""


number = int(input('Ingrese un número entre 0 y el 10: '))
for i in range(1, 11):
    print(f'{number} * {i} = {number * i} ')
