"""

Write a program that determines whether a digit, uppercase, or a lowercase character was entered.

"""

char = input("Enter Digit, Uppercase, or a Lowercase to determine what was entered : ")

if char.isdigit():
    print("YOU TYPED A DIGIT. ")
elif char.isupper():
    print("YOU TYPED AN UPPERCASE CHARACTER. ")
elif char.islower():
    print("YOU TYPED A LOWERCASE CHARACTER. ")
else:
    print("ENTER A VALID INPUT. ")