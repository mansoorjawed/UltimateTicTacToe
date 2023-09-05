import numpy as np
import pygame
from Constants import *

# This function is called whenever a player does a win
# It plays the players move
# Calculates the starting row and column for the next move
# Checks if there are any winners in the microboard
# The return is updated board, the starting and ending of next playable small board,
# and if the move of the player led them to winning in the micro board
def playerMove(row, col, player, gameBoard):
    gameBoard[row][col] = player
    # Formula for calculation last cell in the next boz
    # -> nextEnd = ((position placed % 3) x 3)
    nextStartRow = (row % 3) * 3
    nextStartCol = (col % 3) * 3

    # get the next small 3x3 box for the next box and see if that board is already won
    # get the next small 3x3 box for the next box and see if that board is already won
    microBoard = np.zeros((3, 3))
    microRowStart = (row // 3) * 3
    microColStart = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            microBoard[i][j] = gameBoard[microRowStart + i][microColStart + j]

    microWin = False
    if checkMicroWinner(microBoard):
        microWin = True

    return gameBoard, nextStartRow, nextStartCol, microWin

#Check if a winning condition has been met for someone ot be declared a microWin in the game
def checkMicroWinner(microBoard):
    checker = [microRowWin(microBoard), microColWin(microBoard), microDiagWin(microBoard)]
    return any(checker)

# Check if the columns in the micro board are the same
# as that would declare a winner
def microColWin(microBoard):
    microWin = False
    colNumber = 3
    for i in range(colNumber):
        column = microBoard[:,i]
        compareValues = column == column[0]
        if (column[0] != 0 and compareValues.all()):
            microWin = True
            break

    return microWin

# Check if the rows in the micro board are the same
# as that would declare a winner
def microRowWin(microBoard):
    microWin = False
    for row in microBoard:
        if all(cell == row[0] and cell != 0 for cell in row):
            microWin = True
    return microWin

# Check if the diagonals in the micro board are the same
# as that would declare a winner
def microDiagWin(microBoard):
    microWin = False
    if ((microBoard[0][0] == microBoard[1][1] == microBoard[2][2] != 0)
            or (microBoard[2][0] == microBoard[1][1] == microBoard[0][2] != 0)):
        microWin = True
    return microWin


# helper function to calculate row and column for the availability matrix
def availabilityHelper(bigRow, bigCol):
    row = bigRow % 3
    col = bigCol % 3
    return row, col

# If a micro board is done because of a draw or a player 1, it should be marked unavailable
# so that players are unable to mark anything in the block anymore.
def markUnavailable(bigRow, bigCol, availabilityMatrix):
    row, col =  availabilityHelper(bigRow, bigCol)
    availabilityMatrix[row][col] = False
    print(bigRow, row, bigCol, col, availabilityMatrix)
    return availabilityMatrix

# This if the micro Board the player clicked on is available or not
def isMicroBoardAvailable(bigRow, bigCol, availabilityMatrix):
    row, col = availabilityHelper(bigRow, bigCol)
    return availabilityMatrix[row][col]
