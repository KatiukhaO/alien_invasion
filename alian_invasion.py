import sys

import pygame

from settings import Settings
from ship import Ship
from background import Background
from bullets import Bullet
from alien import Alien


class AlienInvasion:
    """ Class for control resources and behavior of game """

    def __init__(self):
        """ Initialisation of game and creation game resources """
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion", "images/icon_small.bmp")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.background = Background(self)

    def run_game(self):
        """ Run main loop of game """
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            # For each run loop redrawing screen
            self._update_screen()

    def _create_fleet(self):
        """ Create fleet aliens"""
        # Create alien and calculate quantities aliens in row
        # Interval between neighbor aliens is equal width of alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_alians_x = available_space_x // int(2 * alien_width)

        """ Calculate quantities row """
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (2 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        # Create first row aliens
        # Create fleet invasion
        for row_number in range(number_rows):
            for alien_number in range(number_alians_x):
                self._create_aliens(alien_number, alien.rect.size, row_number)


    def _create_aliens(self, alien_number, alien_size, row_number):
        # Create alian and locate him in row
        alien = Alien(self)
        alien_width, alien_height = alien_size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add_internal(alien)

    def _check_fleet_edges(self):

        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):

        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """ Update position all alians in fleet"""
        self._check_fleet_edges()
        self.aliens.update()

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
        elif event.key in (pygame.K_q, pygame.K_ESCAPE):
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """ Respond on dismiss key"""
        if event.key == pygame.K_RIGHT:
            # Move ship right stop
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # Move ship left stop
            self.ship.moving_left = False

    def _fire_bullet(self):
        """ Create new bullet and include him in group bullets"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add_internal(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        # Delete old bullets, which going from border screen
        for bullet in self.bullets:
            if bullet.rect.bottom <= 0:
                self.bullets.remove_internal(bullet)

    def _update_screen(self):
        """ Update picture on screen and show new screen """
        # self.screen.fill(self.settings.bg_color)
        self.background.blitme()
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)
        # Show last drawing screen
        pygame.display.flip()


if __name__ == "__main__":
    # Creation copy class and run game
    ai = AlienInvasion()
    ai.run_game()
