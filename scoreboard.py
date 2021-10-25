import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
    """a class to report scoring infomration"""

    def __init__(
        self, ai_game
    ):  # Next, we give __init__() the ai_game parameter so it can access the settings, screen, and stats objects, which it will need to report the values we’re tracking
        """intialize scorekeeping attributes"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # font settings for scoring infomration
        self.text_color = (30, 30, 30)  # set tect color
        self.font = pygame.font.SysFont(None, 48)  # initiate a font object
        # hiigh score shoiuld never be reset

        # prepare the intial score image
        self.prep_score()  # To turn the text to be displayed into an image, we call prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """turn the score into a rendered image"""
        rounded_score = round(
            self.stats.score, -1
        )  # tells Python to round the value of stats.score to the nearest 10 and store it in rounded_score
        score_str = "{:,}".format(
            rounded_score
        )  # a string formatting directive tells Python to insert commas into numbers when converting a numerical value to a string
        score_str = str(
            self.stats.score
        )  # In prep_score(), we turn the numerical value stats.score into a string
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color
        )  # then pass this string to render(), which creates the image

        # display the score at the top right of the screen.
        self.score_rect = (
            self.score_image.get_rect()
        )  # To make sure the score always lines up with the right side of the screen, we create a rect called score_rect and set its right edge 20 pixels
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = (
            20  # We then place the top edge 20 pixels down from the top of the screen
        )

    def show_score(self):
        """draw score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """turn the high score into a rendeered image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.settings.bg_color
        )

        # center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """check to see if there's a new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        level_str = str(self.stats.level)
        self.level_image = self.font.render(
            level_str, True, self.text_color, self.settings.bg_color
        )

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.level_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """show how many ships are left"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
