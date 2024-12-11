def calcular_monto_pago(categoria, dias_atraso):
    tarifas = {
        'A': {'diaria': 3.00, 'recargo_diario': 1.50, 'max_dias_sin_recargo': 2},
        'B': {'diaria': 2.50, 'recargo_diario': 1.00, 'max_dias_sin_recargo': 3},
        'C': {'diaria': 2.00, 'recargo_diario': 0.50, 'max_dias_sin_recargo': 5},
        # Agrega más categorías según sea necesario
    }

    if categoria in tarifas:
        tarifa_categoria = tarifas[categoria]
        diaria = tarifa_categoria['diaria']
        recargo_diario = tarifa_categoria['recargo_diario']
        max_dias_sin_recargo = tarifa_categoria['max_dias_sin_recargo']

        if dias_atraso <= max_dias_sin_recargo:
            total_pagar = diaria * dias_atraso
        else:
            dias_con_recargo = dias_atraso - max_dias_sin_recargo
            total_pagar = diaria * max_dias_sin_recargo + recargo_diario * dias_con_recargo

        return total_pagar
    else:
        return None

def main():
    # Mostrar categorías de películas
    print("Categorías de películas:")
    print("A - Acción")
    print("B - Comedia")
    print("C - Drama")
    # Agrega más categorías según sea necesario

    # Solicitar al usuario el código de la categoría y el número de días de atraso
    categoria = input("Ingrese el código de la categoría de la película: ").upper()
    dias_atraso = int(input("Ingrese el número de días de atraso: "))

    # Calcular el total a pagar
    total_pagar = calcular_monto_pago(categoria, dias_atraso)

    # Mostrar el resultado
    if total_pagar is not None:
        print(f"Total a pagar: ${total_pagar} dolares")
    else:
        print("Categoría de película no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
