import os
import csv

# read CSV files
def read_csv_folder(folder_path):
    info_dictionary = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, newline='', encoding='latin-1') as csvfile:
                csv_reader = csv.reader(csvfile)
                headers = next(csv_reader, None)
                for row in csv_reader:
                    row = [int(row[0]), int(row[1]), row[2], float(row[3]), int(row[4]),
                           float(row[5]), float(row[6]), float(row[7]), float(row[8]),
                           float(row[9]), float(row[10]), float(row[11]), float(row[12])]
                    product_name = row[2]
                    info_dictionary[product_name] = row
    return info_dictionary


# Folder paths
folder_path1 = r'D:\Python_Exercises\test_oop\frutas'
folder_path2 = r'D:\Python_Exercises\test_oop\verduras'


info_dict1 = read_csv_folder(folder_path1)
info_dict2 = read_csv_folder(folder_path2)

# search in forlde 1
product_to_search = 'Blueberries'
if product_to_search in info_dict1:
    product_info = info_dict1[product_to_search]
    print(f"Information for {product_to_search} in folder 1: {product_info}")
else:
    print(f"No information found for {product_to_search} in folder 1")

# search in folder 2
product_to_search = 'Jitomate'
if product_to_search in info_dict2:
    product_info = info_dict2[product_to_search]
    print(f"Information for {product_to_search} in folder 2: {product_info}")
else:
    print(f"No information found for {product_to_search} in folder 2")
