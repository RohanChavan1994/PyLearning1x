# File handling -> How to read a text file and how to write into it

"""
Open a file ->  file_object = open("filename", mode)
    Modes:
    'r' for reading (default)
    'w' for writing (creates a new file or overwrites over a existing file)
    'a' for appending
    'b' for binary mode
    '+' for updating (reading and writing)

Read a file:
    Reading entire file content -> content = file_object.read() 
    Read single line -> line = file_object.readline()
    Read all lines, saved to a list -> lines = file_object.readlines()

Write to a file:
    Writing string -> file_object.write(string)
    Writing multiple lines -> file_object.writelines(list_of_strings)

Closing a file:
file_object.close()
"""