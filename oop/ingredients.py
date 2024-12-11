# ingredients.py
class Ingredient:
    def __init__(self, id, idGroup, name, portion, idUnit, grossWeight, netWeight, energyK, energyJ, protein, lipids, carbohydrates, fiber):
        self.id = id
        self.idGroup = idGroup
        self.name = name
        self.portion = portion
        self.idUnit = idUnit
        self.grossWeight = grossWeight
        self.netWeight = netWeight
        self.energyK = energyK
        self.energyJ = energyJ
        self.protein = protein
        self.lipids = lipids
        self.carbohydrates = carbohydrates
        self.fiber = fiber

    def __str__(self):
        return f"Ingredient {self.id}: {self.name}\n"\
               f"Portion: {self.portion} | Gross Weight: {self.grossWeight} | Net Weight: {self.netWeight}\n"\
               f"Energy (Kcal): {self.energyK} | Energy (J): {self.energyJ}\n"\
               f"Protein: {self.protein} | Lipids: {self.lipids} | Carbohydrates: {self.carbohydrates} | Fiber: {self.fiber}"
