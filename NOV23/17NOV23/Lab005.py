# with open("text2.txt", "r") as file_obj:
#     content = file_obj.read()
#     print(content)

with open("text2.txt", "r") as file_obj:
    line = file_obj.readline()
    print(line)

with open("text2.txt", "r") as file_obj:
    lines = file_obj.readlines()
    print(lines)
    for x in lines:
        print(x, end="|")
