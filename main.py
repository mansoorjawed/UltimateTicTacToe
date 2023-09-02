import numpy as np
import pygame
import sys
import GameRules

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Board configuration
GRID_SIZE = 3
CELL_SIZE = SCREEN_WIDTH / GRID_SIZE
MINI_CELL_SIZE = CELL_SIZE / GRID_SIZE
BORDER_WIDTH = 2
THICK_BORDER_WIDTH = 4

# Create the Icons
X_ICON = pygame.image.load ('X.png')
X_ICON = pygame.transform.scale(X_ICON, (MINI_CELL_SIZE, MINI_CELL_SIZE))

O_ICON = pygame.image.load('O.png')
O_ICON = pygame.transform.scale(O_ICON, (MINI_CELL_SIZE, MINI_CELL_SIZE))

# Create the screen and clock objects
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ultimate Tic Tac Toe")
clock = pygame.time.Clock()

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


# Main loop
running = True
iconPositions = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse click position and add to the list of icon positions
            x, y = event.pos
            xOfCell = x - (x % MINI_CELL_SIZE)
            yOfCell = y - (y % MINI_CELL_SIZE)

            iconPositions.append((xOfCell, yOfCell))



    screen.fill(WHITE)
    drawBoard()

    for pos in iconPositions:
        print(pos)
        screen.blit(X_ICON, pos)

    pygame.display.flip()
    clock.tick(15)

pygame.quit()
sys.exit()

