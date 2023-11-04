class Car:
    color = None
    model = None

    def car_details(self):
        print("Your car details are ->", self.color, self.model)


car_obj_ref = Car()
car_obj_ref.model = input("Enter car model: ")
car_obj_ref.color = input("Enter car color: ")
car_obj_ref.car_details()
