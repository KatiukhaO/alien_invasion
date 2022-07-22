import sys
from time import sleep

import pygame

from settings import Settings
from ship import Ship
from background import Background
from bullets import Bullet, SuperBullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard


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

        self.stat = GameStats(self)
        self.sb = ScoreBoard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.sbullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.play_button = Button(self, "play")
        self.background = Background(self)
        self.f = True

    def run_game(self):
        """ Run main loop of game """

        while self.f:
            self._check_events()
            if self.stat.game_active:
                self.ship.update()
                self._update_bullets()
                self.sbullets.update()
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
        alien.rect.y = 1.5 * alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):

        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _check_alies_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom > screen_rect.bottom:
                self._ship_hit()
                break

    def _change_fleet_direction(self):

        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """ Update position all aliens in fleet"""
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_alies_bottom()

    def _ship_hit(self):
        if self.stat.ships_left > 0:
            self.stat.ships_left -= 1
            self.sb.prep_ship()

            self.aliens.empty()
            self.bullets.empty()
            self.sbullets.empty()

            self._create_fleet()

            self.ship.center_ship()

            sleep(1)
        else:
            self.stat.game_active = False

    def _check_events(self):
        """Tracking events keyboard and mouses"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos) and not self.stat.game_active:
            #
            self.settings.initialize_dinamic_settings()
            self.stat.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ship()

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
        elif event.key == pygame.K_UP:
            self._fire_bullet()
        elif event.key == pygame.K_SPACE:
            self._fire_super_bullet()

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
            self.bullets.add(new_bullet)

    def _fire_super_bullet(self):
        if len(self.sbullets) < self.settings.sbullets_allowed:
            new_sbullet = SuperBullet(self)
            self.sbullets.add(new_sbullet)

    def _update_bullets(self):
        self.bullets.update()
        # Delete old bullets, which going from border screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self.sbullets.update()
        for sbullet in self.sbullets.copy():
            if sbullet.rect.bottom <= 0:
                self.sbullets.remove(sbullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):

        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        collisionss = pygame.sprite.groupcollide(self.sbullets, self.aliens, True, True)

        if collisionss or collisions:
            for alians in collisionss.values():
                self.stat.score += self.settings.alien_points * len(alians)

            for alians in collisions.values():
                self.stat.score += self.settings.alien_points * len(alians)
            self.sb.prep_score()
            self.sb.check_hight_score()

        if not self.aliens:
            self.bullets.empty()
            self.sbullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stat.level += 1
            self.sb.prep_level()

    def _update_screen(self):
        """ Update picture on screen and show new screen """
        # self.screen.fill(self.settings.bg_color)
        self.background.blitme()
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        for sbullet in self.sbullets.sprites():
            sbullet.draw_bullet()

        self.aliens.draw(self.screen)

        self.sb.show_score()

        # Button Play show if game active
        if not self.stat.game_active:
            self.play_button.draw_buttom()
        # Show last drawing screen
        pygame.display.flip()


if __name__ == "__main__":
    # Creation copy class and run game
    ai = AlienInvasion()
    ai.run_game()
