# Overriding -> Same name in parent and child. Child always overrides the parent functions

class Animal:
    def sound(self):
        print("Animal sound")


class Dog(Animal):
    def sound(self):
        super().sound()  # Super means call my parent function
        print("Dog sound")


animal1 = Animal()
animal1.sound()

dog1 = Dog()
dog1.sound()
