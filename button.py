import pygame.font


class Button():

    def __init__(self, ai_game, msg):
        """ Initialisation atributes button """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Apply size and property button
        self.width, self.height = 200, 50
        self.button_color = (100, 100, 200)
        self.text_color = (255, 255, 255)
        self.font_size = 48
        self.font = pygame.font.SysFont(None, self.font_size)

        # build object RECT for button and set in center screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # message button create only one
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """ Convert msg in rectangle and set text by center """
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_buttom(self):
        # show button
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
