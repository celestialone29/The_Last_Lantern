def process_choice(choice_index, game_state):
    if game_state["step"] == 1:
        if choice_index == 0:  # Enter the mine
            return {
                "description": (
                    "You step into the mine. The air grows colder, and the "
                    "darkness presses against your sight. Without a light, "
                    "you can only make out faint shapes in the shadows."
                ),
                "choices": [
                    "Venture deeper into the dark.",
                    "Search for a light source nearby.",
                    "Turn back toward the entrance."
                ],
                "step": 2
            }
        elif choice_index == 1:  # Search outside the mine
            return {
                "description": (
                    "You search the area outside the mine. Scattered tools "
                    "and broken crates suggest someone left in a hurry. "
                    "Perhaps something useful remains?"
                ),
                "choices": [
                    "Examine the broken crates.",
                    "Inspect the scattered tools.",
                    "Step cautiously into the mine."
                ],
                "step": 2
            }
        elif choice_index == 2:  # Leave the area
            return {
                "description": (
                    "You leave the mine behind. The weight of unanswered "
                    "questions lingers, but for now, you choose safety."
                ),
                "choices": [],
                "step": 3  # End of game for this choice
            }
    elif game_state["step"] == 2:
        if choice_index == 0:  # Venture deeper into the dark
            return {
                "description": (
                    "You venture deeper into the mine, stumbling over loose "
                    "rocks. Without a light, it's too dangerous to continue."
                ),
                "choices": [
                    "Turn back to the entrance.",
                    "Search the area for a light source."
                ],
                "step": 1  # Return to the first step
            }
        elif choice_index == 1:  # Search for a light source
            return {
                "description": (
                    "Inside one of the broken crates, you find an old, rusty "
                    "lantern. It’s in bad shape, but it might still work with "
                    "a little care."
                ),
                "choices": [
                    "Take the lantern and inspect it.",
                    "Search the crates for other supplies.",
                    "Return to the mine entrance."
                ],
                "step": 3  # Progress with the lantern
            }
        elif choice_index == 2:  # Turn back toward the entrance
            return {
                "description": (
                    "You turn back to the mine entrance, the unease gnawing "
                    "at you. The chill of the mine fades slightly as light "
                    "returns."
                ),
                "choices": [
                    "Re-enter the mine cautiously.",
                    "Sit by the entrance to gather your thoughts.",
                    "Leave the area entirely."
                ],
                "step": 1
            }
    elif game_state["step"] == 3:  # With the lantern
        if choice_index == 0:  # Take the lantern and inspect it
            return {
                "description": (
                    "You examine the lantern closely. It’s missing oil, and "
                    "the glass is cracked, but it might still work with some effort."
                ),
                "choices": [
                    "Try to repair the lantern now.",
                    "Search for oil nearby.",
                    "Keep it as-is and enter the mine."
                ],
                "step": 4
            }
        elif choice_index == 1:  # Search for other supplies
            return {
                "description": (
                    "You rummage through the crates but find only splinters "
                    "and dust. It seems the lantern is the only useful item left."
                ),
                "choices": [
                    "Inspect the lantern further.",
                    "Look for more crates elsewhere.",
                    "Step into the mine with the lantern."
                ],
                "step": 3  # Stay on this step
            }
        elif choice_index == 2:  # Return to the mine entrance
            return {
                "description": (
                    "You return to the mine entrance, holding the lantern "
                    "tight. The distant hum of the wind whispers through the tunnel."
                ),
                "choices": [
                    "Prepare to enter the mine.",
                    "Sit by the entrance to gather your thoughts.",
                    "Leave the area entirely."
                ],
                "step": 1
            }
    return None

