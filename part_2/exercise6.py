def calcular_edad(nombre, año_nacimiento, año_actual):
    edad = año_actual - año_nacimiento
    return f'{nombre} cumplirá {edad} años durante el año en curso.'


año_actual = int(input("Ingresa el año en curso: "))
personas = []
for i in range(3):
    nombre = input(f'Ingrese el nombre de la persona {i + 1}: ')
    año_nacimiento = int(input(f'Ingrese el año de nacimiento de {nombre}: '))
    personas.append((nombre, año_nacimiento))

for nombre, año_nacimiento in personas:
    mensaje = calcular_edad(nombre, año_nacimiento, año_actual)
    print(mensaje)
