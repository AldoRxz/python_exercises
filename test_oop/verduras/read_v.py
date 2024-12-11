import csv

# Lista para almacenar la información de cada archivo
listas_informacion = []

# Nombres de los archivos CSV
archivos_csv = ['v_altas_en_potasio.csv', 'v_bajas_en_potasio.csv', 'v_moderadas_en_potasio.csv']

# Iterar sobre cada archivo CSV
for archivo_csv in archivos_csv:
    lista_informacion = []

    # Leer el archivo CSV y almacenar la información en la lista
    with open(archivo_csv, newline='', encoding='latin-1') as csvfile:
        lector_csv = csv.reader(csvfile)
        # Saltar la primera fila si contiene encabezados
        encabezados = next(lector_csv, None)
        for fila in lector_csv:
            # Convertir cada elemento de la fila según su tipo de datos
            fila = [int(fila[0]), int(fila[1]), fila[2], float(fila[3]), int(fila[4]),
                    float(fila[5]), float(fila[6]), float(fila[7]), float(fila[8]),
                    float(fila[9]), float(fila[10]), float(fila[11]), float(fila[12])]
            # Agregar la fila a la lista
            lista_informacion.append(fila)

    # Agregar la lista de información del archivo actual a la lista general
    listas_informacion.append(lista_informacion)

# Imprimir la información de cada archivo
for i, lista_informacion in enumerate(listas_informacion):
    print(f"Información del archivo {i + 1}:")
    for elemento in lista_informacion:
        print(elemento)
    print()
