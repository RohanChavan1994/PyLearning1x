class Person:
    # Attributes
    name = "Harry"  # Public
    _gender = "Male"  # Protected
    __age = 28  # Private

    # Methods
    def print_name(self):
        print(self.name)
        Person.__print_age(self)

    def _print_gender(self):
        print(self._gender)

    def __print_age(self):
        print(self.__age)


person1 = Person()
print(person1.name)
print(person1._gender)
# print(person1.__age)

person1.print_name()
person1._print_gender()
# person1.__print_age()
