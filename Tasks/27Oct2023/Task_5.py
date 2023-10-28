# 5. Write a Python program to count the number of strings in a list where the string length is 2 or more and the
# first and last character are the same.


def count_str(str_list):
    count = 0

    for x in str_list:
        if len(x) > 2 and x[0] == x[-1]:
            count += 1

    return count


str1 = input("Enter a string: ").split(" ")
print("Count of strings with length more than 2 and first and last character are same:", count_str(str1))
