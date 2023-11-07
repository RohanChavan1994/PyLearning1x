class Person:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name, "Age:", self.age)


person1 = Person("Alice", 28)
person2 = Person("Bobby", 26)

print(person1.name, person1.age)
print(person2.name, person2.age)

person1.display()
person2.display()
