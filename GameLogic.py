import numpy as np

def displayBoard(gameBoard):
    # print(map) # map with quote marks
    # Print each element without quote marks
    for row in gameBoard:
        print(' '.join(row))

    return gameBoard

def playerMove(row, col, playerSymbol, gameBoard):
    gameBoard[row][col] = playerSymbol
    displayBoard(gameBoard)

    # Formula for calculation last cell in the next boz
    # -> nextEnd = ((position placed % 3) x 3)
    nextStartRow = (row % 3) * 3
    nextStartCol = (row % 3) * 3

    # get the next small 3x3 box for the next box and see if that board is already won
    microBoard = np.full((3, 3), " ", dtype=str)
    for i in range(3):
        for j in range(3):
            microBoard[i][i] = gameBoard[nextStartRow + i][nextStartCol + j]

    winner = False
    if checkMicroWinner(microBoard):
        winner = True

    return gameBoard, nextStartRow, nextStartCol, winner

#Check if a winning condition has been met for someone ot be declared a winner in the game
def checkMicroWinner(microBoard):
    checker = [microRowWin(microBoard), microColWin(microBoard), microDiagWin(microBoard)]
    return any(checker)

def microColWin(microBoard):
    winner = False
    colNumber = 3
    for i in range(colNumber):
        column = microBoard[:,i]
        compareValues = column == column[0]
        if (column[0] != " " and compareValues.all()):
            winner = True
            break

    return winner

def microRowWin(microBoard):
    winner = False
    for row in microBoard:
        if all(cell == row[0] and cell != " " for cell in row):
            winner = True
    return winner


def microDiagWin(microBoard):
    winner = False
    if ((microBoard[0][0] == microBoard[1][1] == microBoard[2][2] != " ")
            or (microBoard[2][0] == microBoard[1][1] == microBoard[0][2] != " ")):
        winner = True
    return winner

def main():
    players = ["X", "O"]
    moveCount = 0
    gameBoard = np.full((9, 9), " ", dtype=str)


    #Initial first move
    # Has to be outside the loop as it can be placed anywhere on the board
    player = players[((moveCount % 2) + 1)]
    inputMessage = f"Player {player} turn, Enter position: "
    pPosition = input(inputMessage)

    gameBoard, nextStartRow, nextStartCol, winner = playerMove(int(pPosition[:1]), int(pPosition[1:2]), player, gameBoard)

    moveCount += 1

    rows = gameBoard.shape[0]
    columns = gameBoard.shape[1]

    for row in range(rows):
        for col in range(columns):

            nextEndRow = nextStartRow + 2
            nextEndCol = nextStartCol + 2
            # Similar as first move just with a predetermined next micro box based on previous move
            player = players[(moveCount % 2)]
            inputMessage = f"Player {player} turn, Enter position between {nextStartRow}{nextStartCol} and {nextEndRow}{nextEndCol}: "
            pPosition = input(inputMessage)
            row = int(pPosition[:1])
            col = int(pPosition[1:2])
            endRow = row + 2
            endCol =  col + 2
            # restrict values out of the required range of the micro Board
            while (row < nextStartRow or row > endRow
                   or col < nextStartCol or col > endCol):
                pPosition = input(inputMessage)
                row = int(pPosition[:1])
                col = int(pPosition[1:2])
                endRow = row + 2
                endCol = col + 2

            #check micro Winner
            winner = False
            # updated game board and next starting boxes
            gameBoard, nextStartRow, nextStartCol, winner = playerMove(row, col, player, gameBoard)
            print("Micro Won: ", winner)
            moveCount += 1


if __name__ == "__main__":
    main()