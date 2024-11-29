import pygame
import time
from game_state import GameState  # Ensure you have GameState defined in game_state.py

# Initialize pygame
pygame.init()

# Constants for colors
BLACK = (0, 0, 0)
SEPIA = (112, 66, 20)
WHITE = (255, 255, 255)

# Set the window size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("The Last Lantern")

# Load fonts (Make sure the path to your font file is correct)
title_font = pygame.font.Font("fonts/Pieces_of_Eight.ttf", 72)  # Larger font for the title
font = pygame.font.Font("fonts/Pieces_of_Eight.ttf", 48)  # Regular font for game text
small_font = pygame.font.Font("fonts/Pieces_of_Eight.ttf", 24)  # Smaller font for instructions

# Function to render text
def render_text(text, font, color, x, y):
    words = text.split(' ')
    line = ''
    y_offset = y
    max_line_length = 7  # Maximum number of words per line
    for word in words:
        line_width = font.size(line + word)[0] if line else 0
        if line and line_width + font.size(word)[0] <= SCREEN_WIDTH - 40:  # Check if the line fits in the screen
            line += ' ' + word
        else:
            if line:
                text_surface = font.render(line, True, color)
                screen.blit(text_surface, (40, y_offset))
                y_offset += font.get_height()
            line = word  # Start a new line with the current word
    if line:
        text_surface = font.render(line, True, color)
        screen.blit(text_surface, (40, y_offset))
        y_offset += font.get_height()

    return y_offset  # Return the new y_position for the next line

# Function to handle title page
def show_title_page():
    screen.fill(BLACK)
    
    # Show the title page with instructions
    title_text = "The Last Lantern"
    title_width = title_font.size(title_text)[0]
    x_position = (SCREEN_WIDTH - title_width) // 2  # Center the title horizontally
    y_position = 100  # Positioning for title
    y_position = render_text(title_text, title_font, SEPIA, x_position, y_position)  # Larger title
    
    # Instructions for space bar and backspace
    instruction_text = "Press SPACE to continue."
    instruction_width = small_font.size(instruction_text)[0]
    x_position = (SCREEN_WIDTH - instruction_width) // 2  # Center the prompt horizontally
    y_position = render_text(instruction_text, small_font, SEPIA, x_position, y_position)
    
    backspace_text = "Press BACKSPACE to go back a page."
    backspace_width = small_font.size(backspace_text)[0]
    x_position = (SCREEN_WIDTH - backspace_width) // 2
    y_position = render_text(backspace_text, small_font, SEPIA, x_position, y_position)

    pygame.display.update()

# Function to handle choices
def show_choices(choices):
    y_position = SCREEN_HEIGHT - 140  # Ensure choices do not get cut off
    for index, choice in enumerate(choices):
        choice_text = f"{index + 1}. {choice['text']}"  # Add number to each choice
        text_surface = small_font.render(choice_text, True, SEPIA)
        screen.blit(text_surface, (40, y_position))
        y_position += 40
    pygame.display.update()

# Main game loop
def main():
    game_state = GameState()

    # Show title page
    show_title_page()
    
    # Wait for user to press spacebar
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting_for_input = False
                    game_state.current_line = 0  # Reset to the start of the story
                    game_state.text_lines = [
                        "You wake up in the dark, cold mine shaft, your body aching. The air is thick with dust, the sound of dripping water echoing through the tunnels. You can barely see, but you feel something cold and smooth beneath your fingers.",
                        "As your eyes adjust, you make out the faint glow of something in the distance. It’s a lantern, flickering with a dim light. Your heart races as you move toward it, hoping it will guide you out of this nightmare.",
                        "Before you can reach it, you hear a faint sound behind you. A shuffle. A whisper. Is someone else down here with you?",
                    ]  # Example of the story text
                    game_state.choices = []  # Initially no choices until text progresses
                    game_state.choices_progression = [
                        {
                            "text": "Pick up the lantern",
                            "action": lambda: game_state.add_text_lines(["You pick up the lantern, and the faint light illuminates your surroundings. You feel a sense of safety."])
                        },
                        {
                            "text": "Run towards the sound",
                            "action": lambda: game_state.add_text_lines(["You rush towards the sound, heart pounding in your chest. The tunnel stretches endlessly before you."])
                        },
                        {
                            "text": "Hide and wait",
                            "action": lambda: game_state.add_text_lines(["You duck into a small alcove, holding your breath. The sound gets closer, and you tense up, ready for anything."])
                        },
                    ]  # Choices for the player
                    game_state.choices_shown = False  # Choices will not be shown until text progresses

    while game_state.current_line < len(game_state.text_lines):
        screen.fill(BLACK)
        
        # Render the text
        y_position = 50  # Start at the top of the screen
        y_position = render_text(game_state.text_lines[game_state.current_line], font, SEPIA, 40, y_position)
        game_state.current_line += 1
        
        # Show choices if available (only after the last line is displayed)
        if game_state.current_line >= len(game_state.text_lines) and not game_state.choices_shown:
            game_state.choices_shown = True
            show_choices(game_state.choices_progression)
        
        pygame.display.update()

        # Wait for space or backspace
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        waiting_for_input = False
                    elif event.key == pygame.K_BACKSPACE:
                        game_state.process_backspace()  # Go back a page

        # Handle choices after user makes a selection
        if game_state.selected_choice is not None:
            game_state.process_choice(game_state.selected_choice)

    pygame.quit()

if __name__ == "__main__":
    main()

