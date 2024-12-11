class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        area = self.width * self.height
        return area


rectangle1 = Rectangle(5, 10)
area1 = rectangle1.calculate_area()
print(f"Area of rectangle 1: {area1}")

rectangle2 = Rectangle(8, 6)
area2 = rectangle2.calculate_area()
print(f"Area of rectangle 2: {area2}")
