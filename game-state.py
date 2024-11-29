class GameState:
    def __init__(self):
        self.current_line = 0  # Tracks the current story progression
        self.lantern_found = False
        self.waiting_for_help = False
        self.fall_asleep = False

