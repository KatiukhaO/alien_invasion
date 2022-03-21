import sys

import pygame


class AlienInvasion:
    """ Class for control resources and behavior of game """

    def __init__(self):
        """ Initialisation of game and creation game resources """
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """ Run main loop of game """
        while True:
            # Tracking events keyboard and mouses
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Show last drawing screen
            pygame.display.flip()


if __name__ == "__main__":
    # Creation copy class and run game
    ai = AlienInvasion()
    ai.run_game()
