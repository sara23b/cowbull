#a program that gets two numbers and prints the average

a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
#things that you get with input() are always string.
#the function int() is converting string to integer. 
#in order to convert to string, use srt(); in order to convert to integer, use int(); in order to convert to float, use float()


c = a+b/2
#in python. we don't have to determine the type of variables. python will choose an approperiate type.
#here, python determines C to be "float"

print(c)
