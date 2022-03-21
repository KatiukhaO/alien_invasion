import pygame

class Ship():
    """ Class for control ship """

    def __init__(self, ai_game):
        """ Initialisation ship and sets him started position """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Download picture ship and get rectangle
        self.image = pygame.image.load("images/pngwing.com.png")
        self.rect = self.image.get_rect()
        # Each new ship appears in bottom border screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """ Draw ship in current position """
        self.screen.blit(self.image, self.rect)