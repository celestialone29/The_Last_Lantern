from screens import display_text

def progress_story(screen, text_lines, current_line, font):
    display_text(screen, text_lines[current_line], font, 300)
    return current_line + 1

def handle_choice(screen, state, font, choice):
    if state.current_choice == 1:  # First decision: Explore or Wait
        if choice == 1:  # Explore the area
            state.lantern_found = True
            display_text(
                screen,
                "You examine the area and find a small lantern, dented and dusty but intact. "
                "Its glass is smeared with grime, but it looks functional.",
                font,
                300,
            )
            state.current_choice = 2  # Progress to lantern-related choice
        elif choice == 2:  # Wait for help
            if not state.waiting_for_help:
                state.waiting_for_help = True
                display_text(
                    screen,
                    "You decide to wait for help. You curl up, shivering in the damp cold. "
                    "You search your pockets but find only a pen, a crumpled receipt, and a rubber band. "
                    "The minutes stretch into hours, and the cold bites deeper.",
                    font,
                    300,
                )
            elif not state.fall_asleep:
                state.fall_asleep = True
                display_text(
                    screen,
                    "You continue waiting, trembling uncontrollably. Your body grows weak, and you fall asleep. "
                    "You succumb to hypothermia in the darkness. Game Over.",
                    font,
                    300,
                )
                pygame.time.wait(30000)  # Keep the screen open for 30 seconds
    elif state.current_choice == 2:  # Second decision: Lantern actions
        if choice == 1:  # Try to get the lantern working
            state.lantern_on = True
            display_text(
                screen,
                "You fumble with the lantern and manage to ignite the weak oil supply. A faint, flickering light "
                "spreads across the cold stone walls, revealing the jagged edges of the cavern and a faint path "
                "leading deeper into the mine. The air feels slightly less oppressive now.",)
  

