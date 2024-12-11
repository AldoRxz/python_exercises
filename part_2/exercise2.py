def mas_larga(lista_palabras):
    palabra_mas_larga = lista_palabras[0]

    for palabra in lista_palabras[1:]:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra

    return palabra_mas_larga


lista_palabras = ['manzana', 'banana', 'kiwi', 'fresa', 'uva']
resultado_mas_larga = mas_larga(lista_palabras)

print('')
print(f'La palabra más larga en la lista es: {resultado_mas_larga}')
