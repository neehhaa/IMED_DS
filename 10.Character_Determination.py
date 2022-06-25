"""

Write a program that determines whether an alphabet, digit or a whitespace was entered.

"""

char = input("Enter Alphabet, Digit or Space to determine what was entered : ")

if char.isalpha():
    print("YOU TYPED AN ALPHABET. ")
elif char.isdigit():
    print("YOU TYPED A DIGIT. ")
elif char.isspace():
    print("YOU TYPED A SPACE. ")
else:
    print("ENTER A VALID INPUT. ")



