import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """ Class for control ship """

    def __init__(self, ai_game):
        super().__init__()
        """ Initialisation ship and sets him started position """
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Download picture ship and get rectangle
        self.image = pygame.image.load(self.settings.pic_ship)
        self.rect = self.image.get_rect()
        # Each new ship appears in bottom border screen
        self.center_ship()

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Update ship position with flag moving_right """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed_factor

        self.rect.x = self.x

    def blitme(self):
        """ Draw ship in current position """
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        # Save float coordinates center ship
        self.x = float(self.rect.x)
