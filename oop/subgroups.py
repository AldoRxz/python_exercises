# subgroups.py
from ingredients import Ingredient

class Subgroup:
    def __init__(self, name):
        self.name = name
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def get_ingredient_by_id(self, ingredient_id):
        for ingredient in self.ingredients:
            if ingredient.id == ingredient_id:
                return ingredient
        print(f"Ingredient with ID {ingredient_id} not found.")
        return None

    def __str__(self):
        return f"Subgroup: {self.name}\nTotal Ingredients: {len(self.ingredients)}"

    def sum_elements(self, element):
        total = 0
        for ingredient in self.ingredients:
            if hasattr(ingredient, element):
                total += getattr(ingredient, element, 0)
        return total
