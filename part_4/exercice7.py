def is_palindrome(word):
    # Check if a word is a palindrome
    return word == word[::-1]


def inversa(word_list):
    # Find all palindromic words in the list
    palindromes = [word for word in word_list if is_palindrome(word)]
    return palindromes


# Example of usage
word_list = ["radar", "oro", "rajar", "rallar", "salas", "somos", "python"]
palindromic_words = inversa(word_list)

print(f"Palindromic Words in the List:")
print(palindromic_words)
