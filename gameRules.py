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
    return ttt

#Check if a winning condition has been met for someone ot be declared a winner in the game
def checkWinner(ttt):
    win = False
    if colWin() or rowWin(ttt) or diagWin():
        win = True
    return win

def colWin():
    return

# def rowWin(ttt):
#     rowWin = False
#     for row in ttt:
#         for cell in row:
#             if cel
#
#     return

def diagWin():
    return

def main():
    running = True
    while running:
        player1 = "X"
        player2 = "O"
        moveCount = 0

        #mini map
        ttt = np.full((3,3), " ", dtype=str)

        ttt = map(ttt)

        # stop loop false and game not running
        if not running:
            break;

        #check if the game is running
        gameRunning = True
        while gameRunning:
            #player 1 move
            playerCount = (moveCount % 2) + 1
            inputMessage = f"Player {playerCount} turn, Enter position: "
            pPosition = input(inputMessage)

            if playerCount == 1:
                ttt = playerMove(pPosition, player1, ttt)
            else:
                ttt = playerMove(pPosition, player2, ttt)
            moveCount += 1

            # Stop game if 9 moveCount has been played
            if moveCount == 9:
                print("max moves played. Generating new Game: ")
                gameRunning = False
                break


if __name__ == "__main__":
    main()
