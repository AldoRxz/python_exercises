def is_palindromo(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")
    return palabra == palabra[::-1]


print(is_palindromo("radar"))        # True
print(is_palindromo("reconocer"))    # True
print(is_palindromo("python"))       # False
