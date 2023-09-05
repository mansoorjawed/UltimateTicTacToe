import pygame

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Board configuration
GRID_SIZE = 3
CELL_SIZE = SCREEN_WIDTH // GRID_SIZE
MINI_CELL_SIZE = CELL_SIZE // GRID_SIZE
BORDER_WIDTH = 2
THICK_BORDER_WIDTH = 4

# Create the Icons
X_ICON = pygame.image.load ('X.png')
O_ICON = pygame.image.load('O.png')


