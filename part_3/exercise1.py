import random


def aplicar_descuento(total_compra, descuento):
    descuento_aplicado = total_compra * (descuento / 100)
    total_con_descuento = total_compra - descuento_aplicado
    return total_con_descuento


def programa_promocion():
    total_compra = float(input('Ingrese la cantidad total de compras: $'))

    if total_compra < 100.00:
        print('Lo siento, el cliente no aplica a la promoción.')
    else:
        numero_aleatorio = random.randint(0, 5)

        colores = ['blanco', 'rojo', 'verde', 'azul', 'amarillo']
        descuentos = [0, 10, 15, 20, 25]

        color_seleccionado = colores[numero_aleatorio]
        descuento_seleccionado = descuentos[numero_aleatorio]

        print(f'Ha ganado una bola de color {color_seleccionado}.')

        if color_seleccionado != 'blanco':
            total_con_descuento = aplicar_descuento(total_compra, descuento_seleccionado)
            print(f'Descuento del {descuento_seleccionado}% aplicado.')
            print(f"Nuevo total a pagar: ${total_con_descuento}")
        else:
            print(f'No hay descuento aplicado. Total a pagar: $ {total_compra}')


programa_promocion()
