# Collections

# List, Dict, Tuple, Set, OrderedDict

regular = (1,2,3)
# regular[0] = 4 -> Immutable

print(regular[0])

from collections import namedtuple

Person = namedtuple("person", ["name", "age", "gender"])
person1 = Person(name="Rocky", age="28", gender="M")
print(person1)
print('Name:', person1.name)
print('Age:', person1.age)
print('Gender:', person1.gender)


class Person2:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def print_details(self):
        print('Name:', self.name)
        print('Age:', self.age)
        print('Gender:', self.gender)


person2 = Person2("Bondy", 32, "M")
person2.print_details()
