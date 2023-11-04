# Create a Class Person , Two Objects by taking (name, age, address)
# Input from users and print details in the end.

class Person:
    # Attributes
    name = None
    age = None
    address = None

    # Method
    def user_details(self):
        print("User details are: ", self.name, self.age, self.address)


person_obj_ref1 = Person()
person_obj_ref1.name = input("Enter name: ")
person_obj_ref1.age = int(input("Enter age: "))
person_obj_ref1.address = input("Enter address: ")
person_obj_ref1.user_details()

person_obj_ref2 = Person()
person_obj_ref2.name = input("Enter name: ")
person_obj_ref2.age = int(input("Enter age: "))
person_obj_ref2.address = input("Enter address: ")
person_obj_ref2.user_details()
