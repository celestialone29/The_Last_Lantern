import pygame

def render_text(screen, font, text, color, x, y, max_width):
    """Render wrapped text on the screen."""
    words = text.split(' ')
    lines = []
    current_line = ""
    for word in words:
        if len(current_line + word) <= max_width:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    lines.append(current_line.strip())

    y_offset = 0
    for line in lines:
        text_surface = font.render(line, True, color)
        screen.blit(text_surface, (x, y + y_offset))
        y_offset += font.get_linesize()

def render_choices(screen, font, choices, color, x, y):
    """Render a list of choices with numbers."""
    for i, choice in enumerate(choices):
        choice_text = f"{i + 1}. {choice}"
        choice_surface = font.render(choice_text, True, color)
        screen.blit(choice_surface, (x, y + i * font.get_linesize()))

def render_title_page(screen, font_title, font_body):
    """Render the title page with game title and instructions."""
    screen.fill((0, 0, 0))  # Black background
    title_text = "The Last Lantern"
    instruction1 = "Press SPACE to continue"
    instruction2 = "Press BACKSPACE to return"

    title_surface = font_title.render(title_text, True, (205, 133, 63))  # Sepia color
    instruction1_surface = font_body.render(instruction1, True, (205, 133, 63))
    instruction2_surface = font_body.render(instruction2, True, (205, 133, 63))

    screen.blit(title_surface, (screen.get_width() // 2 - title_surface.get_width() // 2, 150))
    screen.blit(instruction1_surface, (screen.get_width() // 2 - instruction1_surface.get_width() // 2, 300))
    screen.blit(instruction2_surface, (screen.get_width() // 2 - instruction2_surface.get_width() // 2, 350))

    pygame.display.flip()

