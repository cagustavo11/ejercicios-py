"""
30. Realiza un programa que calcule las horas transcurridas entre dos horas de dos días de la semana. No se tendrán en cuenta los minutos ni los segundos.
El día de la semana se puede pedir como un número (del 1 al 7) o como una cadena (de “lunes” a “domingo”). Se debe comprobar que el usuario introduce los datos correctamente y que el segundo día es posterior al primero
"""
# pedimos los datos al usuario
num1 = int(input('introduce un número del 1 al 7: '))
num2 = int(input('introduce un número del 1 al 7: '))

hora1 = int(input('ingrese la hora del día uno: '))
hora2 = int(input('ingrese la hora del día dos: '))

hora1 += hora2

total_horas = 0
for _ in range(num1, num2+1):
    total_horas += 24


# Hallamos las horas transcurriadas
horas_transcurridas = total_horas - (hora1 - hora2)
print(f'Las horas transcurridas es: {horas_transcurridas+1}')
