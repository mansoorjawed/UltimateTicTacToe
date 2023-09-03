import numpy as np
import pygame
import sys
from GameLogic import *
from Constants import *

# Initialize pygame
pygame.init()

# Create the Icons
X_ICON = pygame.image.load ('X.png')
O_ICON = pygame.image.load('O.png')

# Scale Icons to appropriate size
X_ICON = pygame.transform.scale(X_ICON, (MINI_CELL_SIZE, MINI_CELL_SIZE))
O_ICON = pygame.transform.scale(O_ICON, (MINI_CELL_SIZE, MINI_CELL_SIZE))
X_ICON_BIG = pygame.transform.scale(O_ICON, (MINI_CELL_SIZE, CELL_SIZE))
O_ICON_BIG = pygame.transform.scale(O_ICON, (MINI_CELL_SIZE, CELL_SIZE))


# Create the screen and clock objects
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ultimate Tic Tac Toe")
clock = pygame.time.Clock()

#Calculate the different values needed basedfrom the mouseclick to determined which cell was clicked
def mouseButtonManager(event):
    # Get mouse click position and add to the list of icon positions
    x, y = event.pos

    # Position of the row and column of the matrix representing the cell
    matrixRow = int(y // MINI_CELL_SIZE)
    matrixCol = int(x // MINI_CELL_SIZE)

    # Position of the starting of the actual cell on the game window
    xOfCell = x - (x % MINI_CELL_SIZE)
    yOfCell = y - (y % MINI_CELL_SIZE)

    return matrixRow, matrixCol, xOfCell, yOfCell

def main():
    # Main loop
    running = True
    iconPositions = []
    smallSymbols = []
    bigSymbols = []
    moveCount = 1
    gameBoardMatrix = np.zeros((9,9))
    players = [1,2]
    startRow = 0
    startCol = 0
    endRow = 8
    endCol = 8


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:

                player = players[(moveCount % 2)]

                row, col, xOfCell, yOfCell = mouseButtonManager(event) #x and Y of the starting of the cell clicked
                # First move allows user to play anywhere on the entire board
                if moveCount != 1:

                    endRow = startRow + 2
                    endCol = startCol + 2
                    if (row >= startRow and row <= endRow
                            and col >= startCol and col <= endCol):
                        gameBoardMatrix, startRow, startCol, winner = playerMove(row, col, player,gameBoardMatrix)
                        print(gameBoardMatrix, winner)

                        iconPositions.append((xOfCell, yOfCell))  # starting on game window of where to put an user symbol
                        # Use a different icon to be placed on the board based on if its player 1 or 2 (rather player 0 or 1)
                        if (player == 1):
                            smallSymbols.append(X_ICON)
                        else:
                            smallSymbols.append(O_ICON)

                        moveCount += 1


                else:
                    moveCount += 1
                    gameBoardMatrix, startRow, startCol, winner = playerMove(row, col, player,gameBoardMatrix)
                    iconPositions.append((xOfCell, yOfCell))  # starting on game window of where to put an user symbol
                    # Use a different icon to be placed on the board based on if its player 1 or 2 (rather player 0 or 1)
                    if (player == 0):
                        smallSymbols.append(X_ICON)
                    else:
                        smallSymbols.append(O_ICON)



        screen.fill(WHITE)
        drawBoard()

        for pos in range(len(iconPositions)):
            screen.blit(smallSymbols[pos], iconPositions[pos])

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()