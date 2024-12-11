# groups.py
from subgroups import Subgroup

class Group:
    def __init__(self, name):
        self.name = name
        self.subgroups = {}

    def add_subgroup(self, subgroup):
        self.subgroups[subgroup.name] = subgroup

    def __str__(self):
        return f"Group: {self.name}\nTotal Subgroups: {len(self.subgroups)}\nSubgroups: {', '.join(self.subgroups.keys())}"
