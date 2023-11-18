# Polymorphism

class Shape:
    def area(self):
        return "Area of shape"


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.142 * self.radius * self.radius


shape1 = Rectangle(4, 5)
print(shape1.area())

shape2 = Circle(4)
print(shape2.area())

shape3 = Shape()
print(shape3.area())
