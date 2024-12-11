import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = math.pi * self.radius**2
        return area

    def calculate_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter


circle1 = Circle(5)
area1 = circle1.calculate_area()
perimeter1 = circle1.calculate_perimeter()
print(f"Area of circle 1: {area1}")
print(f"Perimeter of circle 1: {perimeter1}")

circle2 = Circle(8)
area2 = circle2.calculate_area()
perimeter2 = circle2.calculate_perimeter()
print(f"Area of circle 2: {area2}")
print(f"Perimeter of circle 2: {perimeter2}")
