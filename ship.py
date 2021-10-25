import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_game):
        """initialize the ship and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen  # 1"""A class to manage the ship"""
        self.settings = ai_game.settings  # 1"""A class to manage the ship"
        self.screen_rect = ai_game.screen.get_rect()  # 2
        # load image get its rect
        self.image = pygame.image.load("images/ship.bmp")  # 3
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom  # 4
        self.x = float(
            self.rect.x
        )  # attribute that can hold deciomal values for keeping track of ship's position
        self.moving_right = False  # We add a self.moving_right attribute in the __init__() method and set it to False initially
        self.moving_left = False  # We add a self.moving_left attribute in the __init__() method and set it to False initially

    def update(
        self,
    ):  # Then we add update(), which moves the ship right if the flag is True
        """update the ships postion based on the movement flag."""
        if (
            self.moving_right and self.rect.right < self.screen_rect.right
        ):  # checks for key press and if ship has reached screen edge
            self.rect.x += self.settings.ship_speed  # move ship by amount in settings
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed
        # update rect object from self.x.
        self.rect.x = self.rect.x  # updates ships position

    def blitme(self):  # 5
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """center ship in screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)


""" We import the pygame module before defining the class. The __init__()
method of Ship takes two parameters: the self reference and a reference to
the current instance of the AlienInvasion class''' """
"""At 2 we access the screen’s rect attribute using the get_rect() method
and assign it to self.screen_rect. Doing so allows us to place the ship in the
correct location on the screen."""
""" #3 To load the image, we call pygame.image.load() w and give it the location
of our ship image"""
"""#4 We’ll position the ship at the bottom center of the screen. To do so,
make the value of self.rect.midbottom match the midbottom attribute of the
screen’s rect x."""
"""At #5, we define the blitme() method, which draws the image to the
screen at the position specified by self.rect."""
