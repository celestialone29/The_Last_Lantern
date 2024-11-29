import pygame

def display_text(screen, text, font, y_position, color, width):
    # Code to render the main game text
    lines = wrap_text(text, font, width - 100)
    screen.fill((0, 0, 0))  # Fill the screen with black
    for line in lines:
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect(center=(width // 2, y_position))
        screen.blit(text_surface, text_rect)
        y_position += text_surface.get_height() + 10
    pygame.display.update()

def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + ' ' + word if current_line else word
        test_surface = font.render(test_line, True, (204, 153, 102))

        if test_surface.get_width() <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    lines.append(current_line)
    return lines

def display_title_card(screen, title_font, font, black, sepia):
    title_text = "The Last Lantern"
    prompt_text = "Press Spacebar to Start"

    title_surface = title_font.render(title_text, True, sepia)
    prompt_surface = font.render(prompt_text, True, sepia)

    screen.fill(black)  # Fill background with black
    title_rect = title_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 3))
    prompt_rect = prompt_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    screen.blit(title_surface, title_rect)
    screen.blit(prompt_surface, prompt_rect)

    pygame.display.update()

