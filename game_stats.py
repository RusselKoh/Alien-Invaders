class GameStats:
    # Track stats for game
    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.ships_left = self.ai_settings.ship_limit - 1
        # Start alien in inactive state.
        self.game_active = False
        self.score = 0
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit - 1
        self.score = 0
        self.level = 1
