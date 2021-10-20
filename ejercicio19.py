"""
19. Pedir un número N, introducir N sueldos, y mostrar el sueldo máximo.
"""

cantidadSueldos = int(input('Ingrese la cantidad de suelos a introducir: '))

sueldos = []

for i in range(cantidadSueldos):
    sueldo = int(input('ingrese un sueldo: '))
    sueldos.append(sueldo)

sueldos.sort()
print(f'El sueldo mayor es: {sueldos[-1]}')
