"""
Break with Loops

The break statement in Python is used to terminate the loop or statement in which it is present.
After that, the control will pass to the statements that are present after the break statement,
if available. If the break statement is present in the nested loop, then it terminates only those
loops which contain the break statement.
"""

count = 1
while count <= 10:
    print(count)
    if count == 5:
        break
    count += 1

for counter in range(1, 10):
    if counter == 5:
        break
    print(counter)
print("End of For loop")
