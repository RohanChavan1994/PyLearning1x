try:
    with open("students.txt", "a") as file_obj:
        file_obj.write("Looper\n")
        print(file_obj)
except Exception as error:
    print("Error occurred:", error)
else:
    with open("students.txt", "r") as file_obj:
        print(file_obj.read())
