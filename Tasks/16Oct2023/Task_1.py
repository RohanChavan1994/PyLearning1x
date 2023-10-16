"""
Task #1
✅ Grade Calculator:
Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F)
based on the following grading scale:

input - score - 89
output- B

A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59

If, elif, else
"""

score = float(input("Enter the score: "))

if 90 <= score <= 100:
    print("Grade is A.")
elif 80 <= score <= 89:
    print("Grade is B.")
elif 70 <= score <= 79:
    print("Grade is C.")
elif 60 <= score <= 69:
    print("Grade is D.")
elif 0 <= score <= 59:
    print("Grade is F.")
else:
    print("Error! Enter score from 0 to 100.")
