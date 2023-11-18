# Write to a file

try:
    with open("text1.txt", "w") as file_obj:
        file_obj.write("New Text")
        file_obj.close()
except Exception as error:
    print("Error occurred:", error)
else:
    with open("text1.txt", "r") as file_obj:
        content = file_obj.read()
        print(content)
        file_obj.close()
