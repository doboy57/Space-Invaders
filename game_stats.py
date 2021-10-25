class GameStats:
    """track statistics for alien Invasion"""

    def __init__(self, ai_game):
        """intialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        # start alien invasion in ac acvtive state
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """initialize statistics that can change during game"""
        self.ships_left = self.settings.ship_limit

        self.score = 0
        self.level = 1
