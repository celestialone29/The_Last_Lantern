import pygame
from settings import BLACK, SEPIA

def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + ' ' + word if current_line else word
        test_surface = font.render(test_line, True, SEPIA)
        if test_surface.get_width() <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)
    return lines

def display_text(screen, text, font, y_offset):
    max_width = screen.get_width() - 100
    lines = wrap_text(text, font, max_width)
    screen.fill(BLACK)
    for line in lines:
        text_surface = font.render(line, True, SEPIA)
        screen.blit(text_surface, (50, y_offset))
        y_offset += text_surface.get_height() + 5
    pygame.display.update()

def display_title_card(screen, title_text, prompt_text, title_font, text_font):
    screen.fill(BLACK)
    title_surface = title_font.render(title_text, True, SEPIA)
    prompt_surface = text_font.render(prompt_text, True, SEPIA)
    title_rect = title_surface.get_rect(center=(screen.get_width() / 2, screen.get_height() / 3))
    prompt_rect = prompt_surface.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
    screen.blit(title_surface, title_rect)
    screen.blit(prompt_surface, prompt_rect)
    pygame.display.update()

