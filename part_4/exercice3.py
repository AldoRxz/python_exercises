def ordenada(input_list):
    return all(input_list[i] <= input_list[i + 1] for i in range(len(input_list) - 1))


# examples
lista_ordenada = [1, 2, 3, 4, 5]
lista_no_ordenada = [3, 1, 4, 2, 5]

resultado_ordenada = ordenada(lista_ordenada)
resultado_no_ordenada = ordenada(lista_no_ordenada)

# Imprimir resultados
print(f"¿La lista {lista_ordenada} está ordenada? {resultado_ordenada}")
print(f"¿La lista {lista_no_ordenada} está ordenada? {resultado_no_ordenada}")
