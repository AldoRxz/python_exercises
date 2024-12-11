def multipli(lista):
    producto = 1
    for elemento in lista:
        producto *= elemento
    return producto


def suma(lista):
    producto = 0
    for elemento in lista:
        producto += elemento
    return producto


lista = [1, 2, 3, 4]

resultado_multiplicacion = multipli(lista)
resultado_suma = suma(lista)

print('')
print(resultado_multiplicacion)
print(resultado_suma)
