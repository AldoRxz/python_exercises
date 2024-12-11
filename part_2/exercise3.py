def filtrar_palabras(n, lista):
    palabras_filtradas = []
    for palabra in lista:
        if len(palabra) > n:
            palabras_filtradas.append(palabra)

    return palabras_filtradas


lista_palabras = ['manzana', 'banana', 'kiwi', 'fresa', 'uva']
n = 4
resultado_filtrado = filtrar_palabras(n, lista_palabras)

print('')
print(f'Palabras con más de {n} caracteres: {resultado_filtrado}')
