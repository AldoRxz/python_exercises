def binario_a_entero(numero_binario):
    try:
        entero = int(numero_binario, 2)
        return entero
    except ValueError:
        print("Error: Ingresa un número binario válido.")

binario = "1101"

resultado_entero = binario_a_entero(binario)

print(f"El número binario {binario} es equivalente a {resultado_entero} en entero.")
