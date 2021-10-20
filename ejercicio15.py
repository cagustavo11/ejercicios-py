"""
15. Dadas las edades y alturas de 5 alumnos, mostrar la edad y la estatura media, la cantidad de alumnos mayores de 18 años, y la cantidad de alumnos que miden más de 1.75.
"""


def calcular_media(total_datos, suma_de_datos):
    media = suma_de_datos / total_datos
    return media


# Variables para edades
total_edades = 0
suma_edades = 0

# Variables para estaturas
total_estaturas = 0
suma_estaturas = 0

# Mayores de 18
mayores_18 = 0
# Mayores de 1.75
mayores_175 = 0
for i in range(5):
    edad = int(input('ingrese su edad: '))
    estatura = float(input('ingrese su estatura: '))

    if edad > 18:
        mayores_18 += 1
    if edad > 1.75:
        mayores_175 += 1
    total_edades += edad
    total_estaturas += estatura

media_edad = calcular_media(total_edades, suma_edades)
media_estatura = calcular_media(total_estaturas, suma_estaturas)
print('--------------------------')
print(f'La media de las edades es: {media_edad}')
print(f'La media de las estaturas es: {media_estatura}')
print(f'La cantidad de alumnos mayores de 18 años es: {mayores_18}')
print(f'La cantidad de alumnos que miden más de 1.75 años es: {mayores_175}')
