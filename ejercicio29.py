"""
29. Escribe un programa que permita ir introduciendo una serie indeterminada de números mientras su suma no supere el valor 10000. Cuando esto último ocurra, se debe mostrar el total acumulado, el contador de los números introducidos y la media.
"""


def calcular_media(total_datos, suma_de_datos):
    media = suma_de_datos / total_datos
    return media


cantidad_numeros_introducidos = 0
sumar_numeros = 0
while True:
    num = int(input('introduzca un número: '))

    if sumar_numeros > 100_00:
        break

    sumar_numeros += num
    cantidad_numeros_introducidos += 1

print('--------------------')
print(f'El total acumulado es: {sumar_numeros}')
print(f'Has introducido: {cantidad_numeros_introducidos} números')
print(
    f'La media es: {calcular_media(cantidad_numeros_introducidos, sumar_numeros)}')
