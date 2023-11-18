class Person:
    # Attributes
    name = None
    age = None
    phone_no = None
    height = None
    weight= None
    gender = None
    profession = None

    # Methods
    def talk(self):
        print("Talk")

    def sleep(self):
        print("Sleep")

    def walk(self):
        return "I am walking"


person_obj_ref1 = Person()
person_obj_ref1.name = "Rocky"
person_obj_ref1.age = 28
person_obj_ref1.phone_no = 9876543210
person_obj_ref1.height = 5.11
person_obj_ref1.weight = 83
person_obj_ref1.gender = "Male"
person_obj_ref1.profession = "Engineer"

person_obj_ref1.talk()
person_obj_ref1.sleep()
print(person_obj_ref1.walk())
