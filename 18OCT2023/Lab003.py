"""
Pass -> Skip code
As the name suggests pass statement simply does nothing. The pass statement in Python is used when a statement
is required syntactically, but you do not want any command or code to execute. It is like a null operation,
as nothing will happen if it is executed. Pass statements can also be used for writing empty loops.
Pass is also used for empty control statements, functions, and classes.
"""

for num in range(1,10):
    if num % 2 == 0:
        pass
    else:
        print(f"Found odd number: {num}")
