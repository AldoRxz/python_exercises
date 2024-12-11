def max_of_tree(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


nume1 = 12
nume2 = 14
nume3 = 15
result = max_of_tree(nume1, nume2, nume3)

print('')
print(f'El numero maximo de los siguientes numeros: {nume1}, {nume2} y {nume3} es: {result}')
