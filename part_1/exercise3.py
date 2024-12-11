def longitud(elemento):
    count = 0
    for _ in elemento:
        count += 1
    return count


cadena = 'Hola, mundo!'
lista = [1, 2, 3, 4, 5]

longitud_cadena = longitud(cadena)
longitud_lista = longitud(lista)

print('')
print(f'Longitud de la cadena: {longitud_cadena}')
print(f'Longitud de la lista: {longitud_lista}')
