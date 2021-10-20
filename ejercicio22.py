"""
22. Muestra los números del 320 al 160, contando de 20 en 20 hacia atrás utilizando un bucle for.
Muestra los números del 320 al 160, contando de 20 en 20 hacia atrás utilizando un bucle while
"""

print(f'---------------FOR---------------')
for i in range(320, 140, -20):
    print(i)


print(f'---------------WHILE---------------')
i = 320
while i > 140:
    print(i)
    i -= 20
