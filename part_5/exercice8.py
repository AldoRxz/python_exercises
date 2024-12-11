class WordReverser:
    def reverse_words(self, input_string):
        words = input_string.split()
        reversed_string = ' '.join(reversed(words))
        return reversed_string


reverser = WordReverser()
input_string = "Mi Diario Python"
output_result = reverser.reverse_words(input_string)

print("Entrada:", input_string)
print("Salida:", output_result)
