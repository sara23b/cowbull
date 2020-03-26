#this programs gets a number (N) and prints first N fibonacci numbers

N = int(input("How many of fibbonacci do you want?"))

fibonacci = [] #at first, we make an empty list for fibonacci

fibonacci.append(1) #index = 0
fibonacci.append(1) #index = 1

#this loop will create next fibonacci numbers
i = 2
while i<N:
    fibonacci.append(fibonacci [i-1]+fibonacci[i-2]) #this will make next fibonacci number using 2 past numbers and then stores it in index [i]
    i += 1

for number in fibonacci:
    print(number, end=",") #the usage of "," instead of "\n" for end will show our numbers in one line in the output
