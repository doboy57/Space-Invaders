import pygame

class Ship:
    def __init__ (self, ai_game): 
        self.screen = ai_game.screen #1"""A class to manage the ship"""
        self.screen_rect = ai_game.screen.get_rect() #2 
        #load image get its rect
        self.image = pygame.image.load('images/ship.bmp')#3
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom #4  
    def blitme(self):#5
            self.screen.blit(self.image, self.rect)                                                                                       
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
    
