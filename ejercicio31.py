"""
31. Escribe un programa que, dado un número entero positivo, diga cuáles son y cuánto suman los dígitos pares. Los dígitos pares se deben mostrar en orden, de izquierda a derecha.
Ejemplo:
    Por favor, introduzca un número entero positivo: 04026782
    Digitos pares: 4 0 2 6 8 2
    Suma de los digitos pares: 22
"""

number = input('ingrese un número: ')

# Lista donde estarán todos las cifras de mi número
cifras = []

# Lista vacia en donde guardaré los números pares
pares = []

# Itero sobre el número de tipo string y posteriormente las guarda en un lista ya transformados en números de tipo entero
for i in number:
    cifras.append(int(i))

# Itero la lista de las cifras y las guardo en la lista de números pares
for cifra in cifras:
    if cifra % 2 == 0:
        pares.append(cifra)

# Variable acumuladora
sumar_pares = 0
# Itero sobre los números pares y posteriormente acumulo toda la suma en la variable acumuladora
for par in pares:
    sumar_pares += par

# Imprimo la respuesta
print(f'La suma de cifras que son pares es: {sumar_pares}')
