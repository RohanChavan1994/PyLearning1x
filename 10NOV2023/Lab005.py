# Abstraction
# Hiding details and showing only what is required

# ABC -> Abstract Base Class


from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Bark Bark"


class Cat(Animal):
    def sound(self):
        return "Meow Meow"


class Tiger(Animal):
    def sound(self):
        return "Roar Roar"


dog1 = Dog()
print(dog1.sound())

cat1 = Cat()
print(cat1.sound())

tiger1 = Tiger()
print(tiger1.sound())

# animal1 = Animal()  -> cannot create object

