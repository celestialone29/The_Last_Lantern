class GameState:
    def __init__(self):
        self.state = 0  # Start state
        self.choices = []
        self.description = ""

    def get_description(self):
        # Return descriptions based on the current state
        if self.state == 0:
            self.description = (
                "You are standing at the entrance of an old, abandoned mine shaft. "
                "The air is damp, and the darkness stretches endlessly inside."
            )
            self.choices = ["Enter the mine", "Look around outside", "Leave the area"]
        elif self.state == 1:
            self.description = (
                "You step into the mine. The air grows colder. Faint echoes and the "
                "smell of rust fill the space. Shadows shift with each step."
            )
            self.choices = ["Search for a light source", "Go deeper into the mine", "Examine the walls"]
        elif self.state == 2:
            self.description = (
                "Outside the mine, you notice odd claw marks on the ground. They seem to lead "
                "to a nearby bush, where something glints in the fading sunlight."
            )
            self.choices = ["Investigate the bush", "Look for other tracks", "Go back into the mine"]
        elif self.state == 3:
            self.description = (
                "You decide to leave, but as you walk away, the wind carries a faint whisper. "
                "You feel a chill crawl up your spine."
            )
            self.choices = ["Turn around and head back", "Ignore it and keep walking", "Pause to listen carefully"]
        elif self.state == 4:
            self.description = (
                "You find a broken lantern near the wall. Its glass is shattered, but it might still work if repaired."
            )
            self.choices = ["Try to fix the lantern", "Search for spare parts nearby", "Abandon the lantern"]
        elif self.state == 5:
            self.description = (
                "The sound of your footsteps echoes eerily. Something glimmers faintly in the distance."
            )
            self.choices = ["Approach the glimmer", "Turn back", "Search the ground carefully"]
        elif self.state == 6:
            self.description = (
                "The game has ended. You feel the mine's mysteries pulling you back."
            )
            self.choices = []
        return self.description

    def get_choices(self):
        return self.choices

    def update_state(self, choice):
        # Update the game state based on the player's choice
        if self.state == 0:
            if choice == 0:  # Enter the mine
                self.state = 1
            elif choice == 1:  # Look around outside
                self.state = 2
            elif choice == 2:  # Leave the area
                self.state = 3
        elif self.state == 1:
            if choice == 0:  # Search for a light source
                self.state = 4
            elif choice == 1:  # Go deeper into the mine
                self.state = 5
            elif choice == 2:  # Examine the walls
                self.state = 5  # Transition to the next scenario
        elif self.state == 2:
            if choice == 0:  # Investigate the bush
                self.state = 4
            elif choice == 1:  # Look for other tracks
                self.state = 2
            elif choice == 2:  # Go back into the mine
                self.state = 1
        elif self.state == 3:
            if choice == 0:  # Turn around and head back
                self.state = 1
            elif choice == 1:  # Ignore it and keep walking
                self.state = 6
            elif choice == 2:  # Pause to listen carefully
                self.state = 2

