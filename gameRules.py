import numpy as np
# Defines the game logic and rules by which the game is played.

# Temporary game board before the window is created
# The game works in the consoles with the game map in the console
# First create the large map
# map = np.full((11,11), " ", dtype=str)

# map[:,[3, 7]] = "|" # fill col 3 and 7 with vertical bars
# map[[3,7],:] = "_" # fill row 3 and 7 with horizontal bar



def map(ttt):
    # print(map) # map with quote marks
    # Print each element without quote marks
    for row in ttt:
        print(' '.join(row))

    return ttt

def playerMove(pPosition, playerSymbol, ttt):
    # since there are extra blocks for visualization, should be mindful
    #of entered position
    row = int(pPosition[:1])
    col = int(pPosition[1:2])
    ttt[row, col] = playerSymbol
    map(ttt)
    winner = checkWinner(ttt)
    return ttt, winner

#Check if a winning condition has been met for someone ot be declared a winner in the game
def checkWinner(ttt):
    checker = [rowWin(ttt), colWin(ttt), diagWin(ttt)]
    return any(checker)

def colWin(ttt):
    winner = False
    colNumber = 3
    for i in range(colNumber):
        column = ttt[:,i]
        compareValues = column == column[0]
        if (column[0] != " " and compareValues.all()):
            winner = True
            break

    return winner

def rowWin(ttt):
    winner = False
    for row in ttt:
        if all(cell == row[0] and cell != " " for cell in row):
            winner = True
    return winner


def diagWin(ttt):
    winner = False
    if ((ttt[0][0] == ttt[1][1] == ttt[2][2] != " ")
            or (ttt[2][0] == ttt[1][1] == ttt[0][2] != " ")):
        winner = True
    return winner

def main():

    player1 = "X"
    player2 = "O"
    moveCount = 0
    winner = False

    #mini map
    ttt = np.full((3,3), " ", dtype=str)
    ttt = map(ttt)


    #check if the game is running
    gameRunning = True
    while gameRunning:
        #player 1 move
        playerCount = (moveCount % 2) + 1
        inputMessage = f"Player {playerCount} turn, Enter position: "
        pPosition = input(inputMessage)

        if playerCount == 1:
            ttt, winner = playerMove(pPosition, player1, ttt)
        else:
            ttt, winner = playerMove(pPosition, player2, ttt)
        moveCount += 1
        print(winner)

        # Stop game if 9 moveCount has been played
        if moveCount == 9:
            print("max moves played. Generating new Game: ")
            gameRunning = False
            break


if __name__ == "__main__":
    main()
