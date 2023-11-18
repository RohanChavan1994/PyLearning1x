from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width ) * 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.142 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.142 * self.radius


rect1 = Rectangle(3, 4)
print(rect1.area())
print(rect1.perimeter())

circle1 = Circle(5)
print(circle1.area())
print(circle1.perimeter())
