import pygame


class Background():
    """ Class for control background """

    def __init__(self, ai_game):
        """ Initialisation ship and sets him started position """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Download picture ship and get rectangle
        self.image = pygame.image.load(self.settings.pic_background)
        self.rect = self.image.get_rect()

    def blitme(self):
        """ Draw ship in current position """
        self.screen.blit(self.image, self.rect)
