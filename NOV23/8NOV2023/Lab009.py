# Multiple inheritance

class Father:
    def father_money(self):
        return 5


class Mother:
    def mother_money(self):
        return 5


class Child(Father, Mother):
    def child_money(self):
        return "No money"


child1 = Child()
print(child1.child_money())
print(child1.father_money())
print(child1.mother_money())
