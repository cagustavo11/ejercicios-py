"""
18. Dadas 6 notas, escribir la cantidad de alumnos aprobados (>10), a recuperación ( >= 7) y desaprobados (<7).
"""

aprobados = 0
recuperacion = 0
desaprobados = 0

for i in range(6):
    nota = int(input('ingrese su nota: '))
    if nota > 10:
        aprobados += 1
    if nota >= 7:
        recuperacion += 1
    if nota < 7:
        desaprobados += 1

print(f'La cantidad de alumnos aprobados es: {aprobados}')
print(f'La cantidad de alumnos que irán a recuperacion es: {recuperacion}')
print(f'La cantidad de alumnos que han desaprobado es: {desaprobados}')
