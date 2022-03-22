import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Class for control bullets, released from ship """

    def __init__(self, ai_game):
        super().__init__()
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

class SuperBullet(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.sbullet_color
        self.rect = pygame.Rect(0, 0, self.settings.sbullet_width, self.settings.sbullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def draw_sbullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        """ Moving bullets on the top of screen """
        # Update position bullet in float data format
        self.y -= self.settings.sbullet_speed
        #   Update position rectangle
        self.rect.y = self.y



