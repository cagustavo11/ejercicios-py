"""
28. Realiza un programa que pinte una pirámide por pantalla. La altura se debe pedir por teclado. El carácter con el que se pinta la pirámide también se debe pedir por teclado.
"""
altura = int(input('Ingrese la altura: '))
caracter = input('ingrese un caracte: ')

acumular_espacios = ''
for i in range(1, altura+1):
    print(f'{(caracter + " ") * i}')
