def max_in_list(lista):
    maximo = lista[0]
    for numero in lista[1:]:
        # Comparar cada número en la lista con el máximo actual
        if numero > maximo:
            maximo = numero

    return maximo


def mas_larga(lista_palabras):
    palabra_mas_larga = lista_palabras[0]

    for palabra in lista_palabras[1:]:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra

    return palabra_mas_larga


def filtrar_palabras(n, lista):
    palabras_filtradas = []
    for palabra in lista:
        if len(palabra) > n:
            palabras_filtradas.append(palabra)

    return palabras_filtradas


def contar_mayusculas(cadena):
    contador = 0
    for caracter in cadena:
        if caracter.isupper():
            contador += 1
    return contador


def binario_a_entero(numero_binario):
    entero = int(numero_binario, 2)
    return entero


def calcular_edad(nombre, año_nacimiento, año_actual):
    edad = año_actual - año_nacimiento
    return f"{nombre} cumplirá {edad} años durante el año en curso."


def contar_personas_superior_20(edades):
    cantidad_superior_20 = 0
    for edad in edades:
        if edad > 20:
            cantidad_superior_20 += 1
    return cantidad_superior_20


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


def es_bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)


# Exercise 1
lista_numeros = [12, 5, 8, 19, 3, 15]
resultado_maximo = max_in_list(lista_numeros)

print(f'El número más grande en la lista es: {resultado_maximo}')

# Exercise 2
lista_palabras = ['manzana', 'banana', 'kiwi', 'fresa', 'uva']
resultado_mas_larga = mas_larga(lista_palabras)

print('')
print(f'La palabra más larga en la lista es: {resultado_mas_larga}')

# Exercise 3
lista_palabras = ['manzana', 'banana', 'kiwi', 'fresa', 'uva']
n = 4
resultado_filtrado = filtrar_palabras(n, lista_palabras)

print('')
print(f'Palabras con más de {n} caracteres: {resultado_filtrado}')

# Exercise 4
entrada_usuario = input("Ingresa una cadena: ")

cantidad_mayusculas = contar_mayusculas(entrada_usuario)

print('')
print(f"La cadena tiene {cantidad_mayusculas} letras mayúsculas.")

# Exercise 5
binario = "1101"
resultado_entero = binario_a_entero(binario)

print('')
print(f"El número binario {binario} es equivalente a {resultado_entero} en entero.")

#Exercise 6
año_actual = int(input("Ingresa el año en curso: "))

personas = []
for i in range(3):
    nombre = input(f"Ingrese el nombre de la persona {i + 1}: ")
    año_nacimiento = int(input(f"Ingrese el año de nacimiento de {nombre}: "))
    personas.append((nombre, año_nacimiento))

for nombre, año_nacimiento in personas:
    mensaje = calcular_edad(nombre, año_nacimiento, año_actual)
    print(mensaje)

#Exercise 7
edades_tupla = (18, 25, 30, 22, 19, 21, 26, 23, 20, 28)
resultado_tupla = contar_personas_superior_20(edades_tupla)
print(f"Personas con edades superiores a 20: {resultado_tupla}")

#Agregadas por el usuario
edades_usuario = [int(input(f"Ingrese la edad de la persona {i + 1}: ")) for i in range(10)]
resultado_usuario = contar_personas_superior_20(edades_usuario)
print(f"Personas con edades superiores a 20: {resultado_usuario}")

#Exercise 8


#Exercise 9
palabra_usuario = input("Ingrese una palabra: ")

resultados = contar_vocales(palabra_usuario)
print("Resultados:")
for vocal, cantidad in resultados.items():
    print(f"Letra '{vocal}': {cantidad}")

#Exercise 10
#Ejemplosq [1988, 1992, 1996] son biciestos
año_usuario = int(input("Ingrese un año para verificar si es bisiesto: "))

if es_bisiesto(año_usuario):
    print(f"{año_usuario} es un año bisiesto.")
else:
    print(f"{año_usuario} no es un año bisiesto.")
