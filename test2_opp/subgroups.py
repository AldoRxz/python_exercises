from ingredients import Ingredient  # Importa la clase Ingredient

class Subgroup:
    def __init__(self, name):
        self.name = name
        self.ingredients = []  # Lista para almacenar objetos Ingredient

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def get_ingredient_by_id(self, ingredient_id):
        for ingredient in self.ingredients:
            if ingredient.id == ingredient_id:
                return ingredient
        print(f"Ingredient with ID {ingredient_id} not found in Subgroup {self.name}.")
        return None

    def total_elements_sum(self, element):
        total = 0
        for ingredient in self.ingredients:
            total += float(getattr(ingredient, element, 0))
        return total

    def __str__(self):
        return f"Subgroup: {self.name}, Items: {len(self.ingredients)}"
