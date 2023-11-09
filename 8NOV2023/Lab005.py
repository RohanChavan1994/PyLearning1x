# Single inheritance

class Animal:
    def speak(self):
        print("Animal sound")

    def run(self):
        print("Running...")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def speak(self):
        print("Bark Bark")

    def jog(self):
        Animal().run()


animal1 = Animal()
animal1.speak()
animal1.run()
animal1.eat()

dog1 = Dog()
dog1.speak()
dog1.jog()
dog1.run()
dog1.eat()
