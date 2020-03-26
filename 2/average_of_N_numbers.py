#this program will calculate average of several numbers

numberOfInputs = int(input("How many Numbers are you going to Enter?:"))
i = numberOfInputs
sum = 0

while i>0:
    number = float(input("Type in your number:"))
    sum = sum + number
    i -= 1 

print("Average=",sum/numberOfInputs)