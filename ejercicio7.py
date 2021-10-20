"""
7. Pedir números hasta que se introduzca uno negativo, y calcular la media.
"""


def calcular_media(total_datos, suma_de_datos):
    media = suma_de_datos / total_datos
    return media


sumar_numeros = 0
numeros_introducidos = 0

while True:
    num = int(input('introduzca un número: '))
    if num < 0:
        break
    sumar_numeros += num
    numeros_introducidos += 1

media = calcular_media(numeros_introducidos, sumar_numeros)
print(f'La media es: {round(media, 2)}')
