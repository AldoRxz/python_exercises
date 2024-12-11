import csv

# Nombre del archivo CSV
archivo_csv = 'f_bajas_en_potasio.csv'

lista_informacion = []

with open(archivo_csv, newline='', encoding='latin-1') as csvfile:
    lector_csv = csv.reader(csvfile)
    encabezados = next(lector_csv, None)
    for fila in lector_csv:
        # Convertir cada elemento de la fila según su tipo de datos
        fila = [int(fila[0]), int(fila[1]), fila[2], float(fila[3]), int(fila[4]),
                float(fila[5]), float(fila[6]), float(fila[7]), float(fila[8]),
                float(fila[9]), float(fila[10]), float(fila[11]), float(fila[12])]
        # Agregar la fila a la lista
        lista_informacion.append(fila)

# print
for elemento in lista_informacion:
    print(elemento)
