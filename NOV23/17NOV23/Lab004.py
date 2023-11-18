# Append to a file

try:
    with open("text2.txt", "a") as file_obj:
        file_obj.write("Append Text\n")
        file_obj.close()
except Exception as error:
    print("Error occurred:", error)
else:
    with open("text2.txt", "r") as file_obj:
        content = file_obj.read()
        print(content)
        file_obj.close()
