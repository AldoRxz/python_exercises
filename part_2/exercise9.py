def contar_vocales(palabra):
    contador_a = 0
    contador_e = 0
    contador_i = 0
    contador_o = 0
    contador_u = 0

    for letra in palabra.lower():
        if letra == 'a':
            contador_a += 1
        elif letra == 'e':
            contador_e += 1
        elif letra == 'i':
            contador_i += 1
        elif letra == 'o':
            contador_o += 1
        elif letra == 'u':
            contador_u += 1

    resultados = {
        'a': contador_a,
        'e': contador_e,
        'i': contador_i,
        'o': contador_o,
        'u': contador_u
    }
    return resultados


palabra_usuario = input("Ingrese una palabra: ")

resultados = contar_vocales(palabra_usuario)
print("Resultados:")
for vocal, cantidad in resultados.items():
    print(f"Letra '{vocal}': {cantidad}")
