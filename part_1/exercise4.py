def es_vocal(caracter):
    caracter = caracter.lower()

    return caracter in ['a', 'e', 'i', 'o', 'u']


print('')
print(es_vocal('a'))  # True
print(es_vocal('B'))  # False
print(es_vocal('e'))  # True
print(es_vocal('z'))  # False
