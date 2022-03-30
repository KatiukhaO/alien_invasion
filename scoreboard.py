import pygame.font
from pygame.sprite import Group

from ship import Ship


class ScoreBoard():

    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stat = ai_game.stat

        self.text_color = (255, 255, 255)
        self.bg_color_sb = (0, 0, 0)
        self.font_size = 48
        self.font = pygame.font.SysFont(None, self.font_size)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ship()

    def prep_level(self):

        level_str = f"level : {self.stat.level}"
        self.level_image = self.font.render(level_str, True, self.text_color, self.bg_color_sb)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_score(self):
        rounded_score = round(self.stat.score, -1)
        score_str = f"score : {rounded_score}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.bg_color_sb)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        hight_score = round(self.stat.score, -1)
        hight_score_str = f"max score : {hight_score}"
        self.hight_score_image = self.font.render(hight_score_str, True, self.text_color, self.bg_color_sb)

        self.hight_score_rect = self.hight_score_image.get_rect()
        self.hight_score_rect.centerx = self.screen_rect.centerx
        self.hight_score_rect.top = self.score_rect.top

    def prep_ship(self):

        self.ships = Group()
        for ship_number in range(self.stat.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.hight_score_image, self.hight_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def check_hight_score(self):
        if self.stat.score > self.stat.hight_score:
            self.stat.hight_score = self.stat.score
            self.prep_high_score()
