class my_class:
    def print_my_name_with_last_name(self, name, last_name, age):
        print("Your name is ->", name, last_name, age)

my_class_obj_ref = my_class()
my_class_obj_ref.name = "Rocky"
my_class_obj_ref.print_my_name_with_last_name("Bondy", "Struct", 32)
