import numpy as np
import pygame
from Constants import *
def drawBoard():
    # Draw the mini-grids
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), THICK_BORDER_WIDTH)

            for mini_x in range(1, GRID_SIZE):
                pygame.draw.line(screen, BLACK, (x * CELL_SIZE + mini_x * MINI_CELL_SIZE, y * CELL_SIZE), (x * CELL_SIZE + mini_x * MINI_CELL_SIZE, (y + 1) * CELL_SIZE), BORDER_WIDTH)

            for mini_y in range(1, GRID_SIZE):
                pygame.draw.line(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE + mini_y * MINI_CELL_SIZE), ((x + 1) * CELL_SIZE, y * CELL_SIZE + mini_y * MINI_CELL_SIZE), BORDER_WIDTH)

    # Draw the main grid
    for i in range(1, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, SCREEN_HEIGHT), THICK_BORDER_WIDTH)
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (SCREEN_WIDTH, i * CELL_SIZE), THICK_BORDER_WIDTH)


def playerMove(row, col, player, gameBoard):
    gameBoard[row][col] = player
    # Formula for calculation last cell in the next boz
    # -> nextEnd = ((position placed % 3) x 3)
    nextStartRow = (row % 3) * 3
    nextStartCol = (col % 3) * 3

    # get the next small 3x3 box for the next box and see if that board is already won
    microBoard = np.zeros((3, 3))
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
        if (column[0] != 0 and compareValues.all()):
            winner = True
            break

    return winner

def microRowWin(microBoard):
    winner = False
    for row in microBoard:
        if all(cell == row[0] and cell != 0 for cell in row):
            winner = True
    return winner


def microDiagWin(microBoard):
    winner = False
    if ((microBoard[0][0] == microBoard[1][1] == microBoard[2][2] != 0)
            or (microBoard[2][0] == microBoard[1][1] == microBoard[0][2] != 0)):
        winner = True
    return winner











# def game():
#     players = [1, 2]
#     moveCount = 0
#     gameBoard = np.full((9, 9), " ", dtype=str)
#
#
#     #Initial first move
#     # Has to be outside the loop as it can be placed anywhere on the board
#     player = players[((moveCount % 2) + 1)]
#     inputMessage = f"Player {player} turn, Enter position: "
#     pPosition = input(inputMessage)
#
#     gameBoard, nextStartRow, nextStartCol, winner = playerMove(int(pPosition[:1]), int(pPosition[1:2]), player,
#                                                                gameBoard)
#     moveCount += 1
#
#     rows = gameBoard.shape[0]
#     columns = gameBoard.shape[1]
#
#     for row in range(rows):
#         for col in range(columns):
#
#             nextEndRow = nextStartRow + 2
#             nextEndCol = nextStartCol + 2
#             # Similar as first move just with a predetermined next micro box based on previous move
#             player = players[(moveCount % 2)]
#             inputMessage = f"Player {player} turn, Enter position between {nextStartRow}{nextStartCol} and {nextEndRow}{nextEndCol}: "
#             pPosition = input(inputMessage)
#             row = int(pPosition[:1])
#             col = int(pPosition[1:2])
#             endRow = row + 2
#             endCol =  col + 2
#             # restrict values out of the required range of the micro Board
#             while (row < nextStartRow or row > endRow
#                    or col < nextStartCol or col > endCol):
#                 pPosition = input(inputMessage)
#                 row = int(pPosition[:1])
#                 col = int(pPosition[1:2])
#                 endRow = row + 2
#                 endCol = col + 2
#
#             #check micro Winner
#             winner = False
#             # updated game board and next starting boxes
#             gameBoard, nextStartRow, nextStartCol, winner = playerMove(row, col, player, gameBoard)
#             print("Micro Won: ", winner)
#             moveCount += 1