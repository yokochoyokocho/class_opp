import math


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        area = (self.radius**2) * math.pi
        return round(area, 2)

    def perimeter(self) -> float:
        perimeter = (self.radius * 2) * math.pi
        return round(perimeter, 2)


circle1 = Circle(radius=1)
print(circle1.area())
print(circle1.perimeter())

circle3 = Circle(radius=3)
print(circle3.area())
print(circle3.perimeter())
