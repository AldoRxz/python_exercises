def read_words(file_name):
    try:
        with open(file_name, 'r') as file:
            words = file.read().split()
            return words
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return []


file_name = 'text.txt'
word_list = read_words(file_name)

print(f"Words in the file '{file_name}':")
print(word_list)
