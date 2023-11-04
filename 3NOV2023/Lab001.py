# Class and object in Python


class Dog:
    # breed = None
    # size = None
    # age = None
    # color = None

    def eat(self, breed):
        print(f"{breed} Dog is eating")

    def sleep(self):
        print("Dog is sleeping")

    def sit(self):
        print("Dog is sitting")

    def run(self):
        print("Dog is running")


dog1 = Dog()
dog1.breed = "Neopolitan Mastiff"
dog1.size = "Large"
dog1.age = 5
dog1.color = "Black"

dog1.eat(dog1.breed)
