a = int(input("Type in First Number:"))
b = int(input("Type in Second Number:"))

c = str(int(a/b))
d = str(a%b)

print(c,d, sep="-", end=";")
#print is a function and we can change its behavior. 
#usage of "sep=" indicated what should come instead of "," between variables. by default, sep=" "
#usage of "end=" indicates what should come at the end of print. by default, end="\n"