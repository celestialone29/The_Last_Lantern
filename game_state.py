class GameState:
    def __init__(self):
        self.current_line = 0
        self.text_lines = []  # List to hold the text lines
        self.choices = []  # List to hold the choices
        self.selected_choice = None  # Track the selected choice

    def add_text_lines(self, lines):
        """Add multiple lines of text to the text_lines list."""
        self.text_lines.extend(lines)

    def add_choices(self, choices):
        """Add choices to the choices list."""
        self.choices.extend(choices)

    def process_choice(self, choice_index):
        """Process a choice made by the player."""
        if choice_index < len(self.choices):
            self.selected_choice = choice_index
            choice = self.choices[choice_index]
            choice['action']()  # Execute the action associated with the choice
        self.current_line += 1  # Move to the next line after a choice

    def process_backspace(self):
        """Go back one page of text."""
        if self.current_line > 0:
            self.current_line -= 1

