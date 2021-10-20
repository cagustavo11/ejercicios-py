"""
11. Diseñar un programa que muestre el producto de los 10 primeros números impares.
"""

acumular_producto = 1

for i in range(1, 20, 2):
    acumular_producto *= i

print(
    f'El producto de los 10 primeros números impares es: {acumular_producto}')
