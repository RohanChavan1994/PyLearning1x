# Hybrid inheritance

class A:
    def class_a(self):
        print("This is class A method")


class B(A):
    def class_b(self):
        print("This is class B method")


class C(A):
    def class_c(self):
        print("This is class C method")


class D(B, C):
    def class_d(self):
        print("This is class D method")


d_obj = D()
d_obj.class_d()
d_obj.class_c()
d_obj.class_b()
d_obj.class_a()

c_obj = C()
c_obj.class_c()
c_obj.class_a()

b_obj = B()
b_obj.class_b()
b_obj.class_a()

a_obj = A()
a_obj.class_a()
