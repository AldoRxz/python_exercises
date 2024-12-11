def contar_personas_superior_20(edades):
    cantidad_superior_20 = 0
    for edad in edades:
        if edad > 20:
            cantidad_superior_20 += 1
    return cantidad_superior_20


edades_tupla = (18, 25, 30, 22, 19, 21, 26, 23, 20, 28)
resultado_tupla = contar_personas_superior_20(edades_tupla)
print(f"Personas con edades superiores a 20: {resultado_tupla}")

#Agregadas por el usuario
edades_usuario = [int(input(f"Ingrese la edad de la persona {i + 1}: ")) for i in range(10)]
resultado_usuario = contar_personas_superior_20(edades_usuario)
print(f"Personas con edades superiores a 20: {resultado_usuario}")
