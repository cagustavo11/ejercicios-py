"""
27. Realiza un programa que sume los 100 números siguientes a un número entero introducido por teclado.
"""
number = int(input('Introduce in número: '))


sumar_numeros = 0
for i in range(number, number+101):
    sumar_numeros += i

print(f'La suma es: {sumar_numeros}')
