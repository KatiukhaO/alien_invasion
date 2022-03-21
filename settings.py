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
        self.ship_speed = 1.5

        # Settings bullet
        self.bullet_speed = 1
        self.bullet_pic = "images/bullet_0.png"
