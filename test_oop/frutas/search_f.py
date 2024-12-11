import csv

# CSV file name
csv_file = 'f_bajas_en_potasio.csv'

# Dictionary to store product information
info_dictionary = {}

# Read the CSV file and store information in the dictionary
with open(csv_file, newline='', encoding='latin-1') as csvfile:
    csv_reader = csv.reader(csvfile)
    # Skip the first row if it contains headers
    headers = next(csv_reader, None)
    for row in csv_reader:
        # Convert each element of the row to its respective data type
        row = [int(row[0]), int(row[1]), row[2], float(row[3]), int(row[4]),
               float(row[5]), float(row[6]), float(row[7]), float(row[8]),
               float(row[9]), float(row[10]), float(row[11]), float(row[12])]

        # Get the product name
        product_name = row[2]

        # Store the row in the dictionary using the product name as the key
        info_dictionary[product_name] = row

# search
product_to_search = 'Blueberries'
if product_to_search in info_dictionary:
    product_info = info_dictionary[product_to_search]
    print(f"Information for {product_to_search}: {product_info}")
else:
    print(f"No information found for {product_to_search}")
