def calcular_precio_unitario(codigo):
    # Simulación de una base de datos de productos
    productos = {
        '1': {'nombre': 'Producto1', 'precio': 10.00},
        '2': {'nombre': 'Producto2', 'precio': 15.50},
        '3': {'nombre': 'Producto3', 'precio': 20.00},
        '4': {'nombre': 'Producto3', 'precio': 20.00},
        '5': {'nombre': 'Producto3', 'precio': 20.00},
        '6': {'nombre': 'Producto3', 'precio': 20.00},
        '7': {'nombre': 'Producto3', 'precio': 20.00},
        '8': {'nombre': 'Producto3', 'precio': 20.00},
        '9': {'nombre': 'Producto3', 'precio': 20.00},
        '10': {'nombre': 'Producto3', 'precio': 20.00},
    }

    # Obtener el precio unitario del producto
    if codigo in productos:
        return productos[codigo]['precio']
    else:
        return None


def calcular_total_factura(compras):
    total_factura = sum(cantidad * precio_unitario for codigo, cantidad, precio_unitario in compras)
    return total_factura


def main():
    compras = []

    while True:
        codigo_producto = input("Ingrese el código del producto (o 'fin' para terminar): ")

        if codigo_producto.lower() == 'fin':
            break

        cantidad = int(input("Ingrese la cantidad de unidades: "))

        precio_unitario = calcular_precio_unitario(codigo_producto)

        if precio_unitario is not None:
            compras.append((codigo_producto, cantidad, precio_unitario))
        else:
            print("Código de producto no válido. Inténtelo de nuevo.")

    if not compras:
        print("No se han ingresado productos.")
    else:
        total_factura = calcular_total_factura(compras)
        print("\nFactura:")
        for codigo, cantidad, precio_unitario in compras:
            print(f"{cantidad} unidades de {codigo} - {precio_unitario:.2f} c/u")
        print(f"\nTotal a pagar: ${total_factura:.2f}")


if __name__ == "__main__":
    main()
