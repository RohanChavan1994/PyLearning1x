"""
Task 1
✅ Count vowels and consonants in a String
aeiou

input = pramod
vol = 2
"""


def character_count(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                  'z']
    vowel_count, consonant_count = 0, 0

    for x in string:
        if x.lower() in vowels or x.upper() in vowels:
            vowel_count += 1
        elif x.lower() in consonants or x.upper() in consonants:
            consonant_count += 1

    print("String:", string)
    print(f"Number of vowels:", vowel_count)
    print(f"Number of consonants:", consonant_count)


string = input("Enter a string: ")
character_count(string)
