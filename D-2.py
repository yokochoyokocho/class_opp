import math


class Rectangle:
    def __init__(self, height: float, width: float):
        self.height = height
        self.width = width

    def area(self) -> float:
        area = self.height * self.width
        return round(area, 2)

    def diagonal(self) -> float:
        diagonal = math.sqrt(self.height**2 + self.width**2)
        return round(diagonal, 2)


rectangle1 = Rectangle(height=5, width=6)
print(rectangle1.area())
print(rectangle1.diagonal())

rectangle2 = Rectangle(height=3, width=3)
print(rectangle2.area())
print(rectangle2.diagonal())
