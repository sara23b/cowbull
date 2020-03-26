# this program will tell you if your number is EVEN or not

"""
this is a long comment
i typed several lines
okay, bye.
"""

isEven = False #this is a boolean variable and can be either True or False

number = int(input("Type in your Number:"))

if number%2==0:
    isEven = True

print("Is this an Even number?",isEven)