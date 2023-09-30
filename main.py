import numpy as np
import pygame
import sys
from GameLogic import *
from Constants import *

# Initialize pygame
pygame.init()

# Scale Icons to appropriate size
X_ICON_SMALL = pygame.transform.scale(X_ICON, (MINI_CELL_SIZE, MINI_CELL_SIZE))
O_ICON_SMALL = pygame.transform.scale(O_ICON, (MINI_CELL_SIZE, MINI_CELL_SIZE))
X_ICON_BIG = pygame.transform.scale(X_ICON, (CELL_SIZE, CELL_SIZE))
O_ICON_BIG = pygame.transform.scale(O_ICON, (CELL_SIZE, CELL_SIZE))


# Create the screen and clock objects
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ultimate Tic Tac Toe")
clock = pygame.time.Clock()

#This draws and displays the main Tic Tac Toe game
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
    availabilityMatrix = np.full((3,3), True)
    smallIconPositions = []
    smallIcons = []
    bigIconPositions = []
    bigIcons = []
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
                        gameBoardMatrix, startRow, startCol, microWin = playerMove(row, col, player,gameBoardMatrix)

                        smallIconPositions.append((xOfCell, yOfCell))  # starting on game window of where to put an user symbol
                        # Use a different icon to be placed on the board based on if its player 1 or 2 (rather player 0 or 1)
                        if (not isMicroBoardAvailable(startRow, startCol, availabilityMatrix)):
                            startRow = 0
                            startCol = 0
                            endRow = 8
                            endCol = 8
                        elif (player == 1):
                            smallIcons.append(X_ICON_SMALL)
                        else:
                            smallIcons.append(O_ICON_SMALL)

                        if microWin:
                            markUnavailable(startRow, startCol, availabilityMatrix)
                            bigIconPositions.append((startRow, startCol)) # beginning of the block


                            if (player == 1):
                                bigIcons.append(X_ICON_BIG)
                            else:
                                bigIcons.append(O_ICON_BIG)
                        moveCount += 1

                else:
                    moveCount += 1
                    gameBoardMatrix, startRow, startCol, microWin = playerMove(row, col, player, gameBoardMatrix)
                    smallIconPositions.append((xOfCell, yOfCell))  # starting on game window of where to put an user symbol
                    # Use a different icon to be placed on the board based on if its player 1 or 2 (rather player 0 or 1)
                    if (player == 0):
                        smallIcons.append(X_ICON_SMALL)
                    else:
                        smallIcons.append(O_ICON_SMALL)



        screen.fill(WHITE)
        drawBoard()

        for pos in range(len(smallIconPositions)):
            screen.blit(smallIcons[pos], smallIconPositions[pos])

        for pos in range(len(bigIconPositions)):
            screen.blit(bigIcons[pos], bigIconPositions[pos])

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()