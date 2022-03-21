import sys

import pygame

from settings import Settings
from ship import Ship
from background import Background


class AlienInvasion:
    """ Class for control resources and behavior of game """

    def __init__(self):
        """ Initialisation of game and creation game resources """
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion", "images/icon_small.bmp")

        self.ship = Ship(self)
        self.background = Background(self)

    def run_game(self):
        """ Run main loop of game """
        while True:
            self._check_events()
            self.ship.update()
            # For each run loop redrawing screen
            self._update_screen()

    def _check_events(self):
        """Tracking events keyboard and mouses"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """ Responds on press key"""
        if event.key == pygame.K_RIGHT:
            # Move ship right start
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move ship left start
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """ Respond on dismiss key"""
        if event.key == pygame.K_RIGHT:
            # Move ship right stop
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # Move ship left stop
            self.ship.moving_left = False

    def _update_screen(self):
        """ Update picture on screen and show new screen """
        # self.screen.fill(self.settings.bg_color)
        self.background.blitme()
        self.ship.blitme()
        # Show last drawing screen
        pygame.display.flip()


if __name__ == "__main__":
    # Creation copy class and run game
    ai = AlienInvasion()
    ai.run_game()
