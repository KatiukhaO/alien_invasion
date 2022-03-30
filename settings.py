class Settings():
    """ Class for saved all settings Alian Invasion game"""

    def __init__(self):
        """ Initialisation settings game """
        # Screen parameters
        self.screen_width = 1200
        self.screen_height = 1000
        self.pic_background = "images/background_space.bmp"

        # Settings ship
        self.pic_ship = "images/good_ship_3.png"
        self.ship_speed = 3
        self.ship_limit = 3

        # Settings bullet
        self.bullet_speed = 2.5
        self.bullet_pic = "images/bullet_0.png"
        self.bullets_allowed = 4

        # Settings super bullet
        self.sbullet_speed = 2
        self.sbullets_allowed = 1
        self.sbullet_pic = "images/super_bullet_1.png"

        # Settings alien
        self.pic_alian_ship = "images/bad_ship_1.png"
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # tempo upgrade speed of game
        self.speedup_scale = 3

        self.score_scale = 1.5

        self.initialize_dinamic_settings()

    def initialize_dinamic_settings(self):
        """ initialisation settings and change in during game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0

        # if fleet_direction = 1 it`s move on right , else -1 it`s move on left
        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        """ Update settings of speed """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
