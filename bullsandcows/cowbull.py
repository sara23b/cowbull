
import random

def compare_numbers(number, user_guess):  
    cowbull = [0,0] 
    for i in range(len(number)):
        if number[i] == user_guess[i]:
            cowbull[1]+=1
        else:
            cowbull[0]+=1
    return cowbull


def check(Glist):
    number = Glist[0] 
    guesses = Glist[1] 
    gus = Glist[2]
    k = 0
    while k<5 :
        cowbullcount = compare_numbers(number,gus)
        guesses+=1

        print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

        if cowbullcount[1]==4:
            playing = False
            print("You win the game after " + str(guesses) + "! The number was "+str(number))
            break 
        else:
            print("Your guess isn't quite right, try again.")
        k +=1
    playturn(Glist) 


def playturn(gamelist):
    number = gamelist[0] 
    guesses = gamelist[1] 
    gus = input("guess a 4-digit number:") 
    Glist = [number, guesses, gus]
    check(Glist)



def startgame():
    number = '1234' #str(random.randint(1000,9999))# 
    guesses = 0 
    gamelist = [number, guesses]
    playturn(gamelist)

startgame()
