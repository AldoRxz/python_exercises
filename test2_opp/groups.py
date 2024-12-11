# groups.py
from subgroups import Subgroup

class Group:
    def __init__(self, name):
        self.name = name
        self.subgroups = {}  # Diccionario para almacenar objetos Subgroup

    def add_subgroup(self, subgroup):
        self.subgroups[subgroup.name] = subgroup

    def __str__(self):
        subgroup_info = "\n".join(str(subgroup) for subgroup in self.subgroups.values())
        return f"Group: {self.name}\n{subgroup_info}\nTotal Subgroups: {len(self.subgroups)}"
