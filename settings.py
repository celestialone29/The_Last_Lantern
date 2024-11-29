import pygame

# Initialize pygame
pygame.init()

# Colors
BLACK = (0, 0, 0)
SEPIA = (204, 153, 102)

# Screen dimensions
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

# Fonts
try:
    TITLE_FONT = pygame.font.Font('./fonts/Pieces_of_Eight.ttf', 100)
    TEXT_FONT = pygame.font.Font('./fonts/Pieces_of_Eight.ttf', 40)
except FileNotFoundError:
    print("Font file not found! Ensure it is in the correct path.")
    pygame.quit()
    exit()

