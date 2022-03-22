class Settings():
    """ Class for saved all settings Alian Invasion game"""

    def __init__(self):
        """ Initialisation settings game """
        # Screen parameters
        self.screen_width = 1200
        self.screen_height = 1000
        self.pic_background = "images/background_space.bmp"

        # Settings ship
        self.pic_ship = "images/good_ship_2.png"
        self.ship_speed = 3

        # Settings bullet
        self.bullet_speed = 1.5
        self.bullet_pic = "images/bullet_0.png"
        self.bullets_allowed = 4

        # Settings alien
        self.pic_alian_ship = "images/bad_ship_1.png"
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
