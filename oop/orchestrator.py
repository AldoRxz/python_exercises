from groups import Group
from subgroups import Subgroup
from ingredients import Ingredient
import csv
import os


class Orchestrator:
    def __init__(self, path, folders):
        self.path = path
        self.groups = [Group(folder) for folder in folders]
        # groups = {'verduras': Group(folder_verduras)
        #           'frutas':  Group(folder_frutas)
        # }

    def parse_csv_files(self):
        for group in self.groups:
            group_path = os.path.join(self.path, group.name)

            for filename in os.listdir(group_path):
                if filename.endswith(".csv"):
                    subgroup_name = os.path.splitext(filename)[0]
                    subgroup = Subgroup(subgroup_name)
                    group.add_subgroup(subgroup)

                    with open(os.path.join(group_path, filename), 'r') as csvfile:
                        csv_reader = csv.DictReader(csvfile)
                        for row in csv_reader:
                            ingredient = Ingredient(**row)
                            subgroup.add_ingredient(ingredient)

    def execute(self):
        # Implement the execution logic
        pass


# orc = Orchestrator(path, folder)
# orc.group['verduras'].subgroups['v_bajo_en_potasio'].total_elements_sum('lipids)
