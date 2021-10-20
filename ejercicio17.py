"""
17. Una empresa que se dedica a la venta de desinfectantes necesita un programa para gestionar las facturas. En cada factura figura: el código del artículo, la cantidad vendida en litros y el precio por litro. Se pide de 5 facturas introducidas: Facturación total, cantidad en litros vendidos del artículo 1 y cuantas facturas se emitieron de más de S/600.
"""
import random
codigo_articulo = random.randint(0, 100)


facturacion_total = 0
cantidad_litros = 0
facturas_emitidas_mas_de_600 = 0

for i in range(2):
    precio_por_litro = int(input('ingrese el precio por litro: '))
    litros_vendidos = int(input('ingrese la cantidad vendida en litros: '))

    print('--------------------')
    # calculamos la factura
    factura = precio_por_litro * litros_vendidos
    # condicion si es mayor a 600, lo acumalos en la variable
    if factura > 600:
        facturas_emitidas_mas_de_600 += 1
    # acumulados la factura en la variable acumuladora
    facturacion_total += factura
    # acumulados los litros en la variable acumuladora
    cantidad_litros += litros_vendidos

# imprimos resultados
print(f'La factorizacion total es: {facturacion_total}')
print(f'La cantidad de litros vendidos es: {cantidad_litros}')
print(
    f'La cantidad de facturas mayores a 600 es: {facturas_emitidas_mas_de_600}')
