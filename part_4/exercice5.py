def elimina_duplicados(input_list):
    unique_elements = list(set(input_list))
    return unique_elements


original_list = [1, 2, 3, 2, 4, 5, 3, 6]

unique_list = elimina_duplicados(original_list)

print(f"Original List: {original_list}")
print(f"List with Duplicates Removed: {unique_list}")
