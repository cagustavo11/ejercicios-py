"""
23. Realiza el control de acceso a una caja fuerte. La combinación será un número de 4 cifras. El programa nos pedirá la combinación para abrirla. Si no acertamos, se nos mostrará el mensaje “Lo siento, esa no es la combinación” y si acertamos se nos dirá “La caja fuerte se ha abierto satisfactoriamente”. Tendremos cuatro oportunidades para abrir la caja fuerte.
"""

password = 4055

for i in range(4):
    user_pass = int(input('ingrese la conbinación: '))
    if password == user_pass:
        print("La caja fuerte se ha abierto satisfactoriamente")
        break
    else:
        print("Lo siento, esa no es la combinación")
        break
