#5! = 5 * 4!
#4! = 4 * 3! 
#3! = 3* 2!
#2! = 2 * 1!
#1! = 1 * 0!
#0! = 1
#this program is factorial recursive function
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)

print(factorial(5))
print(factorial(10))