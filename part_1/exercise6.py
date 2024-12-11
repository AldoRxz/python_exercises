def inverse(cadena):
    cadena_invertida = ''
    for caracter in cadena:
        cadena_invertida = caracter + cadena_invertida
    return cadena_invertida


cadena_original = 'estoy probando'
cadena_invertida = inverse(cadena_original)

print('')
print(f'Cadena original: {cadena_original}')
print(f'Cadena invertida: {cadena_invertida}')
