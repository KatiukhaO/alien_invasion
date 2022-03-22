class GameStats():
    """ Treck statistic for game"""
    def __init__(self, ai_game):

        self.settings = ai_game.settings
        self.reset_status()
        self.game_active = True

    def reset_status(self):
        self.ships_left = self.settings.ship_limit