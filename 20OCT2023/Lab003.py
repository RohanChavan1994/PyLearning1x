# Grade calculator using match

score = float(input("Enter the score: "))

match score:
    case score if 90 <= score <= 100:
        print("Grade is A.")
    case score if 80 <= score <= 89:
        print("Grade is B.")
    case score if 70 <= score <= 79:
        print("Grade is C.")
    case score if 60 <= score <= 69:
        print("Grade is D.")
    case score if 0 <= score <= 59:
        print("Grade is F.")
    case _:
        print("Error! Enter score from 0 to 100.")
