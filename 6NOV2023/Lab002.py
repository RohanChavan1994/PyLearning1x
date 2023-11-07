class Person:
    def __init__(self, name):
        self.name = name
        print("You created an object")

    def person_name(self):
        print("Name:", self.name)


person1 = Person("Rocky")
person1.person_name()

person2 = Person("Bondy")
person2.person_name()
