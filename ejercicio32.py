"""
32. Elabore un programa que simule un cajero con acceso a una cuenta de ahorros que permita retiros y depósitos, muestre el saldo al realizar una acción. Utilice la estructura WHILE, el saldo inicial debe ser S/2,000.00.
    • No debe permitir retiros si el monto es mayor al saldo.
    • Debe tener una opción para culminar la sesión.
"""

salto_inicial = 2_000_00

print("La opción para culminar sesion es introducir la letra 'q'")
while True:
    print(f'----------------------')
    opcion = input(
        'Introduce una opción:\n[A] = depositar,\n[B] = retirar,\n[q] = cerrar sesion\nElige => ')

    if opcion.lower() == 'q':
        break

    number = int(input(f'introduzca el saldo: '))

    if number > salto_inicial:
        print(f'No se permite retiros mayores que el saldo')
        continue

    if opcion.lower() == 'a':
        salto_inicial += number

    if opcion.lower() == 'b':
        salto_inicial -= number

    print(f'Su nuevo saldo es: {salto_inicial}')
