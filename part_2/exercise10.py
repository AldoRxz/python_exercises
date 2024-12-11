def es_bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)


#Ejemplosq [1988, 1992, 1996] son biciestos
año_usuario = int(input("Ingrese un año para verificar si es bisiesto: "))

if es_bisiesto(año_usuario):
    print(f"{año_usuario} es un año bisiesto.")
else:
    print(f"{año_usuario} no es un año bisiesto.")
