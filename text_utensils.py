import pygame

def draw_text(text, y_position, font, color, screen, max_width=750):
    """Draw the text on the screen, word wrapping if necessary"""
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + " " + word if current_line else word
        test_text = font.render(test_line, True, color)
        if test_text.get_width() > max_width:  # If the line exceeds screen width, wrap it
            lines.append(current_line)
            current_line = word
        else:
            current_line = test_line
    lines.append(current_line)  # Add the last line

    y_offset = y_position
    for line in lines:
        text_surface = font.render(line, True, color)
        screen.blit(text_surface, (25, y_offset))
        y_offset += text_surface.get_height() + 5

