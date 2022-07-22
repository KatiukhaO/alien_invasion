class GameStats():
    """ Track statistic for game"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_status()
        # Game run in nonactive staged
        self.game_active = False
        self.hight_score = 0

    def reset_status(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
