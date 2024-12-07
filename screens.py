import pygame
from text_utils import render_text
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, TEXT_COLOR

# Screen class for displaying the title page, story, and choices
class Screen:
    def __init__(self, screen):
        self.screen = screen

    def show_title_page(self):
        self.screen.fill((0, 0, 0))  # Black background
        render_text("The Last Lantern", pygame.font.Font("fonts/Pieces_of_Eight.ttf", 72), TEXT_COLOR, 150, 100, self.screen)
        render_text("Press SPACE to start", pygame.font.Font("fonts/Pieces_of_Eight.ttf", 24), TEXT_COLOR, 150, SCREEN_HEIGHT - 100, self.screen)
        pygame.display.update()

