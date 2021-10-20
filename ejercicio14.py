"""
14. Pedir 10 sueldos. Mostrar su suma y cuantos hay mayores de S/1,000.
"""

mayores_de_1000 = 0
suma_total = 0

for i in range(10):

    sueldo = int(input('Ingrese su sueldo: '))
    if sueldo > 1000:
        mayores_de_1000 += 1
    suma_total += sueldo
print(f'La suma total de los sueldos es: {suma_total}')
print(f'La cantidad de sueldos mayores a 1000 son: {mayores_de_1000}')
