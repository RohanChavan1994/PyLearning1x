### Task #1
#### _1. Explain the difference between the = operator and the == operator in Python._
##### = is the assignment operator. It sets a particular variable equal to a particular value (or another variable).
###### _For example:_
###### c = 5
###### We are declaring the c variable, and assigning it the value of 5.
#
##### == is the equality operator. It is used in true/false expressions to check whether one value is equal to another one. The equality operator doesn’t set any value, it only checks whether two values are equal.
###### _For example:_
###### (2 + 2) == 5 evaluates to false, since 2 + 2 = 4, and 4 is not equal to 5.
#
#
#### _2. What does the ** operator do in Python, and how is it used ?_
##### Double asterisks (**) acts as an exponentiation operator for numeric values. ** operator is lightweight as compared to the pow() function because functions takes more processing and compilation power (because it takes parameters and has multiple statements embedded within it) than this operator.
###### _For example:_
###### a = 2
###### b = 6
###### c = a ** b
###### print("The required output is {0}".format(c))
#
#
#### _3. What does the ^ operator do in Python, and in what context is it commonly used ?_
##### Bitwise XOR (exclusive OR) -> Each bit position in the result is the logical XOR of the bits in the corresponding position of the operands. 1 if the bits in the operands are different, 0 if they’re equal.
###### _For example:_
###### print(6 ^ 3)

###### The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

###### 6 = 0000000000000110
###### 3 = 0000000000000011
###### --------------------
###### 5 = 0000000000000101
###### ====================
#
###### A bitwise operator works with the binary representation of a number rather than that number's value. The operand is treated as a set of bits, instead of as a single number.
#
###### Most regular operators work with either single or multiple bytes, which in most systems contain eight bits. A bitwise operator is a character representing an action that works on data at the bit level rather than with bytes or larger units of data. Because they allow greater precision and require fewer resources, bitwise operators can make some code faster and more efficient.
#
###### Examples of uses of bitwise operations include encryption, compression, graphics, communications over ports/sockets, embedded systems programming and finite state machines.