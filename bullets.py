import  pygame
from pygame.sprite import Sprite


class Bullet():
    """ Class for control bullets, released from ship """

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load(self.settings.bullet_pic)
        self.rect = self.image.get_rect()

        # Create bullet in position (0, 0) and set correct position
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        """ Moving bullets on the top of screen """
        # Update position bullet in float data format
        self.y -= self.settings.bullet_speed
        #   Update position rectangle
        self.rect.y = self.y

    def draw_bullet(self):
        """ Output pullets on the display"""
        self.screen.blit(self.image, self.rect)
