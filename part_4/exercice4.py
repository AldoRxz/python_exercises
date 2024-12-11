import random


def duplicado(input_list):
    # Utiliza un conjunto para verificar duplicados eficientemente
    seen = set()
    for element in input_list:
        if element in seen:
            return True
        seen.add(element)
    return False


def generate_random_list():
    # Genera una lista de 23 números aleatorios del 1 al 100
    return random.sample(range(1, 101), 23)


# Part A - Testing "duplicado" function with a sample list
sample_list = [1, 2, 3, 4, 5, 2, 6, 7, 8]
result_a = duplicado(sample_list)
print(f"Does the list {sample_list} have duplicates? {result_a}")

# Part B - Generating a random list and testing for duplicates
random_list = generate_random_list()
result_b = duplicado(random_list)
print(f"Does the random list have duplicates? {result_b}")
