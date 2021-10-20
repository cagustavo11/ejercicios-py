"""
10. Pedir 10 números y escribir la suma total.
"""
acumular_numeros = 0
for i in range(10):
    number = int(input('ingrese un número: '))
    acumular_numeros += number

print(f'La suma total de los números es: {acumular_numeros}')
