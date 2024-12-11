def contar_mayusculas(cadena):
    contador = 0
    for caracter in cadena:
        if caracter.isupper():
            contador += 1
    return contador


entrada_usuario = input("Ingresa una cadena: ")

cantidad_mayusculas = contar_mayusculas(entrada_usuario)

print('')
print(f"La cadena tiene {cantidad_mayusculas} letras mayúsculas.")
