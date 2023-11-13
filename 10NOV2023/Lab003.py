# Method Overloading

class MathUtil:
    def add(self, a=0, b=0, c=0):
        return a + b + c


math1 = MathUtil()
print(math1.add(1, 2))
print(math1.add(1, 2, 3))
