"""
Continue with Loops

Continue is also a loop control statement just like the break statement. continue statement is opposite to that
of the break statement, instead of terminating the loop, it forces to execute the next iteration of the loop.
As the name suggests the continue statement forces the loop to continue or execute the next iteration.
When the continue statement is executed in the loop, the code inside the loop following the continue statement
will be skipped and the next iteration of the loop will begin.
"""

for num in range(1, 10):
    if num % 2 == 0:
        print(f"Found even number: {num}")
        continue
    print(f"Found odd number: {num}")
