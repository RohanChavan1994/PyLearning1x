def say_hello():
    print("Hello")


say_hello()


def func_with_param(a):
    return a ** 2


print(func_with_param(4))

# Lambda expression

msg = lambda: print("Hello")
msg()

text = lambda a: a ** 2
print(text(4))
