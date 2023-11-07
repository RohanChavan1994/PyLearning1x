class Car:  # Only one constructor can be used in a class
    make = None
    model = None

    def __init__(self):
        print("Default constructor", self.name)

    def __init__(self, make, model):
        self.make = make
        self.model = model
        print("Parameterized constructor", make, model)

    def start_engine(self):
        print("Start engine", self.make, self.model)


car1 = Car("VW", "Virtus")  # When an object is created, a special method is called automatically ->  __init__()
# All the attributes of the object can be initialized -> add some initial value to them

print(id(car1))
car2 = Car("Honda", "Civic")
print(id(car2))

car1.start_engine()
car2.start_engine()