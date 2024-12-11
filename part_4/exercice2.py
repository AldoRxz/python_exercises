def elimina(input_list):
    if len(input_list) < 2:
        return []
    else:
        return input_list[1:-1]


def midle(input_list):
    if len(input_list) < 2:
        return []
    else:
        return input_list[1:-1]


original_list = [1, 2, 3, 4, 5]
result_elimina = elimina(original_list)
result_media = midle(original_list)

print("Original List:", original_list)
print("Result of 'elimina':", result_elimina)
print("Result of 'media':", result_media)
