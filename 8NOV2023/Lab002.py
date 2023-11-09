class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def print_details(self):
        print("Your details:", self.__name, self.__age)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


person1 = Person("Rocky", 28)
person1.print_details()
print(person1.get_name())
print(person1.get_age())

person1.set_name("Bondy")
person1.set_age(32)

person1.print_details()
print(person1.get_name())
print(person1.get_age())
