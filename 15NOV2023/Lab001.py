# Exception -> Abnormal event during the program execution. It can be handled.

# Error -> Problem with specific code. Mistake by developers.
# It is very difficult to overcome

print("Start")

try:
    a = 10/0
except Exception as error:
    print("Error occurred:", error)
else:
    print(a)
finally:
    print("This is finally block")

print("End")
