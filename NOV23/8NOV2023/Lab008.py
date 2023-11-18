# Hierarchical inheritance

class TwoWheeler:
    def info(self):
        print("This is Two Wheeler class")

    def details(self):
        print("I have 2 wheels")


class Bike(TwoWheeler):
    def info(self):
        print("This is bike class")


class Bicycle(TwoWheeler):
    def info(self):
        print("This is bicycle class")


bike1 = Bike()
bike1.info()
bike1.details()

bicycle1 = Bicycle()
bicycle1.info()
bicycle1.details()

two_wheeler1 = TwoWheeler()
two_wheeler1.info()
two_wheeler1.details()
