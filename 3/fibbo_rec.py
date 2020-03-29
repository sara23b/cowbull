#recursive fibbonacci function
#fibbo(5) = fibbo(4)+fibbo(3)
#fibbo(4) = fibbo(3)+fibbo(2)
#fibbo(3) = fibbo(2)+fibbo(1)
#fibbo(2) = fibbo(1)+fibbo(0)
#fibbo(1) & fibbo(0) = 1

def fibbo_recursive(number):
    if number == 1 or number == 0:
        return 1
    else:
        return fibbo_recursive(number-1)+fibbo_recursive(number-2)

print(fibbo_recursive(5)) #=5
print(fibbo_recursive(6)) #=8
print(fibbo_recursive(7)) #=13