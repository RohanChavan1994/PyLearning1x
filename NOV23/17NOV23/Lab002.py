# Read a file

try:
    with open("text1.txt", "r") as file_obj:
        content = file_obj.read()
        print(content)
except Exception as error:
    print("Error occurred:", error)
