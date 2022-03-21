class Settings():
    """ Class for saved all settings Alian Invasion game"""

    def __init__(self):
        """ Initialisation settings game """
        # Screen parameters
        self.screen_width = 1200
        self.screen_height = 1000
        # Set background color
        self.bg_color = (230, 230, 230)
        self.pic_background = "images/background_space.bmp"

        # Settings ship
        self.pic_ship = "images/good_ship_2.png"
        self.ship_speed = 1.5
