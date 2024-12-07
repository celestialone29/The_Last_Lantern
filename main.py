import pygame
from game_logic import process_choice

pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("The Last Lantern")

# Colors
COLOR_SEPIA = (112, 66, 20)

# Fonts
font_title = pygame.font.Font("fonts/Pieces_of_Eight.ttf", 48)
font_body = pygame.font.Font("fonts/Pieces_of_Eight.ttf", 28)

# Initial game state
game_state = {
    "step": 1,
    "description": "You find yourself at the entrance to a dark, abandoned mine shaft.",
    "choices": [
        "Search the crates nearby.",
        "Enter the mine carefully.",
        "Leave the area."
    ],
}

# History to track previous states
history = []

# Helper functions
def render_text(surface, font, text, x, y, max_width):
    words = text.split()
    lines = []
    current_line = []
    current_width = 0

    for word in words:
        word_width = font.size(word + " ")[0]
        if current_width + word_width <= max_width:
            current_line.append(word)
            current_width += word_width
        else:
            lines.append(" ".join(current_line))
            current_line = [word]
            current_width = word_width
    if current_line:
        lines.append(" ".join(current_line))

    for i, line in enumerate(lines):
        text_surface = font.render(line, True, COLOR_SEPIA)
        surface.blit(text_surface, (x, y + i * font.get_linesize()))

def render_choices(surface, font, choices, x, y):
    for i, choice in enumerate(choices):
        text_surface = font.render(f"{i + 1}. {choice}", True, COLOR_SEPIA)
        surface.blit(text_surface, (x, y + i * font.get_linesize()))

def render_title_page():
    screen.fill((0, 0, 0))
    render_text(screen, font_title, "The Last Lantern", 50, 100, SCREEN_WIDTH - 100)
    render_text(screen, font_body, "Press SPACE to continue", 50, 300, SCREEN_WIDTH - 100)
    render_text(screen, font_body, "Press BACKSPACE to exit", 50, 350, SCREEN_WIDTH - 100)
    pygame.display.flip()

# Main loop
def main():
    running = True
    at_title = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if at_title:
                    if event.key == pygame.K_SPACE:
                        at_title = False
                    elif event.key == pygame.K_BACKSPACE:
                        running = False
                else:
                    if event.key == pygame.K_BACKSPACE:
                        if history:
                            # Go back one step in history
                            previous_state = history.pop()
                            game_state.update(previous_state)
                        else:
                            # If no history, go back to the title screen
                            at_title = True
                    elif event.unicode.isdigit():
                        choice_index = int(event.unicode) - 1
                        history.append(game_state.copy())  # Save current state before moving forward
                        new_state = process_choice(choice_index, game_state)
                        if new_state:
                            game_state.update(new_state)

        if at_title:
            render_title_page()
        else:
            screen.fill((0, 0, 0))
            render_text(screen, font_body, game_state["description"], 50, 50, SCREEN_WIDTH - 100)
            render_choices(screen, font_body, game_state["choices"], 50, 400)
            pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

