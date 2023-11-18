# Multi-level inheritance

class Grandparent:
    def grandparent_method(self):
        print("Grandparent's method")


class Parent(Grandparent):
    def parent_method(self):
        print("Parent's method")


class Child(Parent):
    def child_method(self):
        print("Child's method")


child1 = Child()
child1.child_method()
child1.parent_method()
child1.grandparent_method()

parent1 = Parent()
parent1.parent_method()
parent1.grandparent_method()

grandparent1 = Grandparent()
grandparent1.grandparent_method()
