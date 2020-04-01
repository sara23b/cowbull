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
    elif board[2] == board[5] and board[2]==board[8] and board[2]!="[]":
        return True
    elif board[3] == board[6] and board[3]==board[9] and board[3]!="[]":
        return True
    elif board[1] == board[5] and board[1]==board[9] and board[1]!="[]":
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
def getAIMove(board):
    if board[1] == "[]" :
        if board[2] == board[3] or board[4] == board[7] or board[5] == board[9] :
            board[1] = "O"
    elif board[2] == "[]":
        if board[5] == board[8] or board[1] == board[3]:
            board[2] = "O"
    elif board[3] == "[]":
        if board[1] == board[2] or board[5] == board[7] or board[6] == board[9]:
            board[3] = "O"
    elif board[4] == "[]":
        if board[1] == board[7] or board[5] == board[6]:
            board[4] = "O"
    elif board[5] == "[]":
        if board[2] == board[8] or board[3] == board[7] or board[1] == board[9] or board[4] == board[6]:
            board[5] = "O"
    elif board[6] == "[]":
        if board[3] == board[9] or board[5] == board[4]:
            board[6] = "O"
    elif board[7] == "[]":
        if board[8] == board[9] or board[4] == board[1] or board[5] == board[3]:
            board[7] = "O"
    elif board[8] == "[]":
        if board[5] == board[2] or board[7] == board[9]:
            board[8] = "O"
    elif board[9] == "[]":
        if board[5] == board[1] or board[6] == board[3] or board[8] == board[7]:
            board[9] = "O"                                                                
    else:
        random = "O"                

def playAITurn(board):  
    getAIMove(board)
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