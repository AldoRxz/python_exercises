def max_in_list(lista):
    maximo = lista[0]
    for numero in lista[1:]:
        # Comparar cada número en la lista con el máximo actual
        if numero > maximo:
            maximo = numero

    return maximo


lista_numeros = [12, 5, 8, 19, 3, 15]
resultado_maximo = max_in_list(lista_numeros)

print(f'El número más grande en la lista es: {resultado_maximo}')
