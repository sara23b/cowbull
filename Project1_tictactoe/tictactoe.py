#tic tac toe project
import random
import os

def showTheBoard(board):
    os.system('cls')
    print(board[7],board[8],board[9])
    print(board[4],board[5],board[6])
    print(board[1],board[2],board[3])

def getPlayerMove(board):
    choice = int(input("Which Tile?"))
    if board[choice] != "[]":
        print("this tile is occupied, choose another one")
        getPlayerMove(board)
    else:
        board[choice] = "X"

def checkForWin(board):
    if board[1] == board[2] and board[1]==board[3] and board[1]!="[]":
        return True
    elif board[4] == board[5] and board[4]==board[6] and board[4]!="[]":
        return True
    elif board[7] == board[8] and board[7]==board[9] and board[7]!="[]":
        return True
    elif board[1] == board[4] and board[1]==board[7] and board[1]!="[]":
        return True
    elif board[2] == board[5] and board[2]==board[8] and board[4]!="[]":
        return True
    elif board[3] == board[6] and board[3]==board[9] and board[3]!="[]":
        return True
    elif board[1] == board[5] and board[1]==board[9] and board[4]!="[]":
        return True
    elif board[3] == board[7] and board[3]==board[9] and board[3]!="[]":
        return True
    else:
        return False

def endGame(winner):
    if winner=="Tie":
        print("It's a Tie")
    else:
        print(winner,"won!")
    choice = input("Do you want to play again?(y/n)")
    if choice == "y":
        startGame()

def checkForTie(board):
    isTie = True
    n = 1
    while n<10:
        if board[n] == "[]":
            isTie = False
    return isTie

def playHumanTurn(board):
    showTheBoard(board)
    getPlayerMove(board)
    if checkForWin(board):
        endGame("Human")
    else:
        if checkForTie(board):
            endGame("Tie")
        else:
            playAITurn(board)

def playAITurn(board):
    #here goes your code!
    #based on the flowchart, complete this function so we can play the game
    getAIMove(board) #--> you should write this function
    if checkForWin(board):
        endGame("Computer")
    else:
        if checkForTie(board):
            endGame("Tie")
        else:
            playHumanTurn(board)

def startGame():
    board = {1:"[]", 2:"[]", 3:"[]", 4:"[]", 5:"[]", 6:"[]", 7:"[]", 8:"[]", 9:"[]"}
    isHumanTurn = random.choice([True, False])

    if isHumanTurn:
        playHumanTurn(board)
    else:
        playAITurn(board)