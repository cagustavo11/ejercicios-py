"""
12. Pedir un número y calcular su factorial (no utilice la formula).
"""


def factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial


num = int(input('Ingrese un número: '))
res = factorial(num)

print(f'El factorial es: {res}')
