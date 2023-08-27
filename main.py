import pygame

# Initialize pygame
pygame.init()

# Get screen dimensions
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h


# Calculate percentage-based dimensions
def calculate_dimensions(percentage, total_dimension):
    return int(percentage * total_dimension / 100)


# Percentage-based dimensions for game window
game_window_width_percentage = 50
game_window_height_percentage = 50

game_window_width = calculate_dimensions(game_window_width_percentage, screen_width)
game_window_height = calculate_dimensions(game_window_height_percentage, screen_height)

# Create the game window
screen = pygame.display.set_mode((game_window_width, game_window_height))
pygame.display.set_caption("Tic Tac Toe")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Your game drawing code goes here

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
