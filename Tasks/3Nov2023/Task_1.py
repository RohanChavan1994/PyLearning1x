# Create a Car class and Create 2 Objects of the class with attributes 5 and 5 methods

class Car:
    # Attributes
    company = None
    name = None
    model = None
    type = None
    color = None

    # Methods
    def start_car(self):
        print("Starting car -> ", self.model, self.color, self.company, self.name, self.type)

    def drive(self):
        print("Driving car -> ", self.model, self.color, self.company, self.name, self.type)

    def cruise(self):
        print("Cruising car -> ", self.model, self.color, self.company, self.name, self.type)

    def brake(self):
        print("Braking car -> ", self.model, self.color, self.company, self.name, self.type)

    def turn_off(self):
        print("Turn off car -> ", self.model, self.color, self.company, self.name, self.type)


car_obj_ref1 = Car()
car_obj_ref1.model = 2020
car_obj_ref1.color = "Black"
car_obj_ref1.company = "Hyundai"
car_obj_ref1.name = "i20"
car_obj_ref1.type = "Hatchback"
car_obj_ref1.start_car()
car_obj_ref1.drive()
car_obj_ref1.cruise()
car_obj_ref1.brake()
car_obj_ref1.turn_off()

car_obj_ref2 = Car()
car_obj_ref2.model = 2016
car_obj_ref2.color = "Red"
car_obj_ref2.company = "Ford"
car_obj_ref2.name = "Figo Aspire"
car_obj_ref2.type = "Sedan"
car_obj_ref2.start_car()
car_obj_ref2.drive()
car_obj_ref2.cruise()
car_obj_ref2.brake()
car_obj_ref2.turn_off()
