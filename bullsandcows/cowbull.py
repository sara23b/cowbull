
import random

def finish():
    print("Game Over!")
    choice = input("Do you want to play Again?(y/n)")
    if choice == 'y':
        startGame()

def compare_numbers(number, gus):  
    cowbull = [0,0] 
    for i in range(0 , 4):
        if number[i]== gus[i]:
            cowbull[1]+=1
    for i in number:
        if i in gus:
            cowbull[0]+=1
    cowbull[0] = cowbull[0]-cowbull[1]
    return cowbull


def check(Glist):
    number = Glist[0] 
    guesses = Glist[1] 
    gus = Glist[2]
    Number = Glist[3]
    cowbullcount = compare_numbers(number,gus)
    guesses+=1

    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + "! The number was "+str(Number))
        finish()
    else:
        print("Your guess isn't quite right, try again.")
    gamelist = [Number, number, guesses]
    playturn(gamelist) 


def playturn(gamelist):
    Number = gamelist[0]
    number = gamelist[1] 
    guesses = gamelist[2] 
    guess = input("guess a 4-digit number:") 
    gus = [int(x) for x in str(guess)]
    Glist = [number, guesses, gus, Number]
    check(Glist)



def startgame():
    Number = "1234" #str(random.randint(1000,9999))#
    number = [int(x) for x in str(Number)]
    guesses = 0 
    gamelist = [ Number,number, guesses]
    playturn(gamelist)

startgame()
