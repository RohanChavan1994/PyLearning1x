# Single inheritance

class Parent:
    name = "Bobby"


class Child(Parent):
    name1 = "Turbo"


child1 = Child()
print(child1.name)
print(child1.name1)

parent1 = Parent()
print(parent1.name)
