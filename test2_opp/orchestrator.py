# orchestrator.py
import os
import csv
from groups import Group
from subgroups import Subgroup
from ingredients import Ingredient


class Orchestrator:
    def __init__(self, path, folders):
        self.path = path
        self.folders = folders
        self.groups = {}

    def parse_csv(self, file_path):
        ingredients = []
        with open(file_path, 'r', encoding='latin-1') as file:
            reader = csv.DictReader(file)
            for row in reader:
                ingredient = Ingredient(**row)
                ingredients.append(ingredient)
        return ingredients

    def print_all_groups_subgroups(self):
        for group_name, group in self.groups.items():
            print(f"Group: {group_name}")
            for subgroup_name, subgroup in group.subgroups.items():
                print(f"  Subgroup: {subgroup_name}")
        print("\nEnd of groups and subgroups.")

    def execute(self):
        for folder in self.folders:
            group = Group(folder)
            folder_path = os.path.join(self.path, folder)

            for filename in os.listdir(folder_path):
                if filename.endswith(".csv"):
                    file_path = os.path.join(folder_path, filename)
                    subgroup = Subgroup(filename)

                    ingredients = self.parse_csv(file_path)
                    subgroup.ingredients.extend(ingredients)

                    group.add_subgroup(subgroup)

            self.groups[folder] = group

    def get_group_by_name(self, group_name):
        return self.groups.get(group_name)

    def query_group_subgroup(self, group_name, subgroup_name, element):
        group = self.get_group_by_name(group_name)
        if group:
            subgroup = group.subgroups.get(subgroup_name)
            if subgroup:
                total = subgroup.total_elements_sum(element)
                return total
            else:
                print(f"Subgroup {subgroup_name} not found in Group {group_name}.")
        else:
            print(f"Group {group_name} not found.")
        return None

    def __str__(self):
        group_info = "\n".join(str(group) for group in self.groups.values())
        return f"Orchestrator Info:\n{group_info}\nTotal Groups: {len(self.groups)}"
