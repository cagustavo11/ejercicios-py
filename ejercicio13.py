"""
13. Pedir 10 números. Mostrar la media de los números positivos, la media de los números negativos y la cantidad de ceros.
"""


def calcular_media(total_datos, suma_de_datos):
    media = suma_de_datos / total_datos
    return media


numeros_positivos = []
numeros_negativos = []

cantidad_ceros = 0

# Pedimos 10 números
for i in range(10):
    num = int(input('ingrese un número: '))
    if num > 0:
        numeros_positivos.append(num)
    if num < 0:
        numeros_negativos.append(num)
    if num == 0:
        cantidad_ceros += 1


# Variable acumuladora
sumar_positivos = 0
# Iteramos por los numeros positivos
for numero_positivo in numeros_positivos:
    sumar_positivos += numero_positivo

# Ejecutamos nuestra función que calcula la media
media_positivos = calcular_media(len(numeros_positivos), sumar_positivos)
# imprimimos la respuesta
print(f'La media de los positivos es: {media_positivos}')

# Variable acumuladora
sumar_negativos = 0
# Iteramos por los numeros negativos
for numero_negativo in numeros_negativos:
    sumar_negativos += numero_negativo

media_negativos = calcular_media(len(numeros_negativos), sumar_negativos)
print(f'La media de los negativos es: {media_negativos}')
