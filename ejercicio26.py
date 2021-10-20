"""
26. Escribe un programa que diga si un número introducido por teclado es o no primo. Un número primo es aquel que sólo es divisible entre él mismo y la unidad.
"""

number = int(input('Introduce un número: '))

acumular_veces = 0
for i in range(1, number+1):
    if number % i == 0:
        acumular_veces += 1

if acumular_veces == 2:
    print(f'El número SÍ es primo!')
else:
    print(f'El número NO es primo')
