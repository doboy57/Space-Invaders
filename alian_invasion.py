import sys  # use to exit game when player quits
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet 


class AlienInvasion:
    """overall class to manage game assets and behavior"""

    def __init__(self):
        """intialize the game, andcreate game resources"""
        pygame.init()  # initializes the background settings that Pygame needs to work properly
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width #gets screen width and updates settings
        self.settings.screen_height = self.screen.get_rect().height
        # create a display window, on which we’ll draw all the game’s graphical elements.settinfs pulled from settings.py
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(
            self
        )  # import ship and then make an instance after screen is created
        self.bullets = pygame.sprite.Group()
        self.bg_color = (230, 230, 230)  # set the color of the game window

    def run_game(
        self,
    ):  # The game is controlled by the run_game() method. This method contains a while loop w that runs continually. The while loop contains an event loop and code that manages screen updates. An event is an action that the user performs while playing the game, such as pressing a key or moving the mouse. To make our program respond to events, we write this event loop to listen for events and perform appropriate tasks depending on the kinds of events that occur.
        """start the main loop for the game"""
        while True:
            self._check_events()  # To call a method from within a class, use dot notation with the variable self and the name of the method
            self.ship.update()
            self.bullets.update()
            self._update_screen()

    def _check_events(
        self
    ):  # We make a new _check_events() method v and move the lines that check whether the player has clicked to close the window into this new method
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # we add an elif block to the event loop to respond when Pygame detects a KEYDOWN event
                self._check_keydown_events(event)  # check whether the key pressed, event.key, is the right arrow key
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event) # check whether the key released, event
    def _check_keydown_events(self, event): # helper method
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True #instead of changing the ship’s position directly, we merely set moving_right to True 
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q: #game quites if you press q 
            sys.exit()
        elif event.key ==pygame.K_SPACE:
            self._fire_bullet()
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False #instead of changing the ship postion directly to stop moving we set to false
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False 
    def _fire_bullet(self):
        """create a new bullet and add it to the bullets group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


                   
    def _update_screen(
        self,
    ):  # """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()  # after filling backround ship appears on top of background
        # redraw the screen during each pass through the game loop (pulled from savings file )
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == "__main__":
    # make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
