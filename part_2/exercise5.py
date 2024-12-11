def binario_a_entero(numero_binario):
    entero = int(numero_binario, 2)
    return entero


binario = "1101"
resultado_entero = binario_a_entero(binario)

print('')
print(f"El número binario {binario} es equivalente a {resultado_entero} en entero.")
