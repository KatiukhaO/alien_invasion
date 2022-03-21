import sys

import pygame

<<<<<<< HEAD
from settings import Settings

=======
>>>>>>> 2c35b5f55ca66c5d7728e7708f617b9e0aac60fe

class AlienInvasion:
    """ Class for control resources and behavior of game """

    def __init__(self):
        """ Initialisation of game and creation game resources """
        pygame.init()
<<<<<<< HEAD
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
=======

        self.screen = pygame.display.set_mode((1200, 800))
>>>>>>> 2c35b5f55ca66c5d7728e7708f617b9e0aac60fe
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """ Run main loop of game """
        while True:
            # Tracking events keyboard and mouses
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

<<<<<<< HEAD
            # For each run loop redrawing screen
            self.screen.fill(self.settings.bg_color)

=======
>>>>>>> 2c35b5f55ca66c5d7728e7708f617b9e0aac60fe
            # Show last drawing screen
            pygame.display.flip()


if __name__ == "__main__":
    # Creation copy class and run game
    ai = AlienInvasion()
    ai.run_game()
