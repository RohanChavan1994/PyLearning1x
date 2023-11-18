class A:
    def method(self):
        print("This is class A method")


class B:
    def method(self):
        print("This is class B method")


class C(A, B):
    pass


class D(B, A):
    pass


c_obj = C()
c_obj.method()

d_obj = D()
d_obj.method()
