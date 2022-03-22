import  pygame

class Alien:

    def __init__(self, ai_game):

        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load(self.settings.pic_alian_ship)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)


    def draw_alien(self):
        """ Output pullets on the display"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left."""
        self.x += (self.settings.alien_speed *
                        self.settings.fleet_direction)
        self.rect.x = self.x