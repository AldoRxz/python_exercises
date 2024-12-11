def superposition(lista1, lista2):
    for elemento_lista1 in lista1:
        for elemento_lista2 in lista2:
            if elemento_lista1 == elemento_lista2:
                return True
    return False


lista_a = [1, 2, 3, 4, 5]
lista_b = [5, 6, 7, 8, 9]

resultado = superposition(lista_a, lista_b)
print('')
print(resultado)
