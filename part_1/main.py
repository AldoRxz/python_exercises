def maxi(a, b):
    if a > b:
        return a
    else:
        return b


def max_of_tree(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


def longitud(elemento):
    count = 0
    for _ in elemento:
        count += 1
    return count


def es_vocal(caracter):
    caracter = caracter.lower()

    return caracter in ['a', 'e', 'i', 'o', 'u']


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


def inverse(cadena):
    cadena_invertida = ''
    for caracter in cadena:
        cadena_invertida = caracter + cadena_invertida
    return cadena_invertida


def is_palindromo(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")
    return palabra == palabra[::-1]


def superposition(lista1, lista2):
    for elemento_lista1 in lista1:
        for elemento_lista2 in lista2:
            if elemento_lista1 == elemento_lista2:
                return True
    return False


def generate_n_characters(n, caracter2):
    resultado = caracter2*n
    return resultado


def procedure(lista2):
    for numero in lista2:
        print('*' * numero)

#Exercise 1
num1 = 10
num2 = 20
result = maxi(num1, num2)

print(f'El máximo entre {num1} y {num2} es: {result}')

#Exercise 2
nume1 = 12
nume2 = 14
nume3 = 15
result = max_of_tree(nume1, nume2, nume3)

print('')
print(f'El numero maximo de los siguientes numeros: {nume1}, {nume2} y {nume3} es: {result}')

#Exersice 3
cadena = 'Hola, mundo!'
lista = [1, 2, 3, 4, 5]

longitud_cadena = longitud(cadena)
longitud_lista = longitud(lista)

print('')
print(f'Longitud de la cadena: {longitud_cadena}')
print(f'Longitud de la lista: {longitud_lista}')

#Exersice 4
print('')
print(es_vocal('a'))  # True
print(es_vocal('B'))  # False
print(es_vocal('e'))  # True
print(es_vocal('z'))  # False

#Exersice 5
lista = [1, 2, 3, 4]

resultado_multiplicacion = multipli(lista)
resultado_suma = suma(lista)

print('')
print(resultado_multiplicacion)
print(resultado_suma)

#Exersice 6
cadena_original = 'estoy probando'
cadena_invertida = inverse(cadena_original)

print('')
print(f'Cadena original: {cadena_original}')
print(f'Cadena invertida: {cadena_invertida}')

#Exersice 7
print('')
print(is_palindromo("radar"))        # True
print(is_palindromo("reconocer"))    # True
print(is_palindromo("python"))       # False

#Exersice 8
lista_a = [1, 2, 3, 4, 5]
lista_b = [5, 6, 7, 8, 9]

resultado = superposition(lista_a, lista_b)
print('')
print(resultado)

#Exersice 9
n = 5
caracter = "x"
resultado_generado = generate_n_characters(n, caracter)

print('')
print(resultado_generado)

#Exersice 10
lista_procedure = [4, 9, 7]
print('')
procedure(lista_procedure)

