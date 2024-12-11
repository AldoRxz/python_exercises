def count_names_starting_with_letter(names, letter):
    # Filter names that start with the specified letter
    filtered_names = [name for name in names if name.lower().startswith(letter.lower())]

    # Print the count of names
    print(f"The number of names starting with '{letter}' is: {len(filtered_names)}")

# List of names
names_list = ["Alice", "Bob", "Charlie", "David", "Emma", "Alex", "Anna", "Amanda"]

# Print the list of names
print("List of names:", names_list)

user_letter = input("Enter a letter to count names starting with: ")

# Validate user input (ensure it's a single letter)
if len(user_letter) == 1 and user_letter.isalpha():
    # Count and print names starting with the user-specified letter
    count_names_starting_with_letter(names_list, user_letter)
else:
    print("Please enter a valid single letter.")
