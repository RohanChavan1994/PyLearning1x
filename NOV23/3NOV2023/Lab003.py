class Car:
    name = None
    color = None
    model = None
    speed = None
    engine = None

    def start_engine(self):
        print(f"Starting engine of {self.name}")

    def drive(self):
        print("Driving")

    def brake(self):
        print("Applying brakes")


car_obj_ref1 = Car()
car_obj_ref1.name = "Ford"
car_obj_ref1.start_engine()
car_obj_ref1.drive()
car_obj_ref1.brake()

car_obj_ref2 = Car()
car_obj_ref2.model = 2012
car_obj_ref2.name = "VW"
car_obj_ref2.start_engine()
