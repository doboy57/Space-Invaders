import sys  # use to exit game when player quits
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """overall class to manage game assets and behavior"""

    def __init__(self):
        """intialize the game, andcreate game resources"""
        pygame.init()  # initializes the background settings that Pygame needs to work properly
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        # create a display window, on which we’ll draw all the game’s graphical elements.settinfs pulled from settings.py
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self) #import ship and then make an instance after screen is created
        self.bg_color = (230, 230, 230)  # set the color of the game window

    def run_game(
        self,
    ):  # The game is controlled by the run_game() method. This method contains a while loop w that runs continually. The while loop contains an event loop and code that manages screen updates. An event is an action that the user performs while playing the game, such as pressing a key or moving the mouse. To make our program respond to events, we write this event loop to listen for events and perform appropriate tasks depending on the kinds of events that occur.
        """start the main loop for the game"""
        while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()#after filling backround ship appears on top of background 
            # redraw the screen during each pass through the game loop (pulled from savings file )

            # make the most recently drawn screen visible
            pygame.display.flip()


if __name__ == "__main__":
    # make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
