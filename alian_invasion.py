import sys  # use to exit game when player quits
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """overall class to manage game assets and behavior"""

    def __init__(self):
        """intialize the game, andcreate game resources"""
        pygame.init()  # initializes the background settings that Pygame needs to work properly
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = (
            self.screen.get_rect().width
        )  # gets screen width and updates settings
        self.settings.screen_height = self.screen.get_rect().height
        # create a display window, on which we’ll draw all the game’s graphical elements.settinfs pulled from settings.py
        pygame.display.set_caption("Alien Invasion")

        # create an instance to store game statistics
        # and create a scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(
            self
        )  # import ship and then make an instance after screen is created
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        # make the play button
        self.play_button = Button(self, "Play")
        self.bg_color = (230, 230, 230)  # set the color of the game window

    def run_game(
        self,
    ):  # The game is controlled by the run_game() method. This method contains a while loop w that runs continually. The while loop contains an event loop and code that manages screen updates. An event is an action that the user performs while playing the game, such as pressing a key or moving the mouse. To make our program respond to events, we write this event loop to listen for events and perform appropriate tasks depending on the kinds of events that occur.
        """start the main loop for the game"""
        while True:
            self._check_events()  # To call a method from within a class, use dot notation with the variable self and the name of the method
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    def _update_bullets(self):
        """update postion of bullets and get rud of old bullets"""
        # update bullet postion
        self.bullets.update()
        # get rid of bullets that have disappeared
        for (
            bullet
        ) in (
            self.bullets.copy()
        ):  # We use the copy() method to set up the for loop u, which enables us to modify bullets inside the loop
            if (
                bullet.rect.bottom <= 0
            ):  # We check each bullet to see whether it has disappeared off the top of the screen at
                self.bullets.remove(bullet)  # If it has, we remove it from bullets
            self._check_bullet_alien_collisions()
            print(
                len(self.bullets)
            )  # At x we insert a print() call to show how many bullets currently exist in the game and verify that they’re being deleted when they reach the top of the screen
            # Check for any bullets that have hit aliens.
            # If so, get rid of the bullet and the alien.

    def _check_bullet_alien_collisions(self):
        """respond to bullet-alien collisions"""
        # remove any bullets and aliens that have collided
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens:
            # destroy existing bullets and create new fleet
            self.bullets.empty()  # check if alien group is empty
            self._create_fleet()  # respawn aliens
            self.settings.increase_speed()
            # Increase level
            self.stats.level += 1
            self.sb.prep_level()

    def _check_events(
        self,
    ):  # We make a new _check_events() method v and move the lines that check whether the player has clicked to close the window into this new method
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif (
                event.type == pygame.KEYDOWN
            ):  # we add an elif block to the event loop to respond when Pygame detects a KEYDOWN event
                self._check_keydown_events(
                    event
                )  # check whether the key pressed, event.key, is the right arrow key
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)  # check whether the key released, event
            elif (
                event.type == pygame.MOUSEBUTTONDOWN
            ):  # Pygame detects a MOUSEBUTTONDOWN event when the player clicks anywhere on the screen
                mouse_pos = (
                    pygame.mouse.get_pos()
                )  # To accomplish this, we use pygame.mouse.get_pos(),which returns a tuple containing the mouse cursor’s x- and y-coordinates when the mouse button is clicked
                self._check_play_button(
                    mouse_pos
                )  # We send these values to the new method _check_play_button()

    def _check_keydown_events(self, event):  # helper method
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True  # instead of changing the ship’s position directly, we merely set moving_right to True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:  # game quites if you press q
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()  # call fire bullet when space bar is pressed

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False  # instead of changing the ship postion directly to stop moving we set to false
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)  # create instance of bullet call it new bullet
            self.bullets.add(new_bullet)  # add new bullet to bullets group

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        avaliable_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = avaliable_space_x // (2 * alien_width)
        # determine the number of rows of aliens that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (
            self.settings.screen_height - (3 * alien_height) - ship_height
        )
        number_rows = available_space_y // (2 * alien_height)
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """create alien place in row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """respond if any aliens have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """drops the entire fleet and change the feelts direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(
        self,
    ):  # """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()  # after filling backround ship appears on top of background
        # redraw the screen during each pass through the game loop (pulled from savings file )
        for (
            bullet
        ) in (
            self.bullets.sprites()
        ):  # To draw all fired bullets to the screen, we loop through the sprites in bullets and call draw_bullet() on each one
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # draw the score information
        self.sb.show_score()
        if not self.stats.game_active:
            self.play_button.draw_button()
        # make the most recently drawn screen visible
        pygame.display.flip()

    def _update_aliens(
        self,
    ):
        """update the positions of all aliens in the fleet"""
        """check if the fleet is at an edge,then update the position of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()
        # look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()
        print("ship hit!!!")

    def _ship_hit(self):  # Inside _ship_hit(), the number of ships left is reduced by 1
        """respond to the ship being hit by an alien"""
        if self.stats.ships_left > 0:
            # Decrement ships_left
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # get rid of any remaining aliens and bullets
            self.aliens.empty()  # after which we empty the groups aliens and bullets
            self.bullets.empty()
            # create a new fleet and center the ship
            self._create_fleet()  # Next, we create a new fleet and center the ship
            self.ship.center_ship()

            # pause
            sleep(
                0.5
            )  # Then we add a pause after the updates have been made to all the game elements but before any changes have been drawn to the screen, so the player can see that their ship has been hit
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """check if any aliens have reached the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if (
                alien.rect.bottom >= screen_rect.bottom
            ):  # An alien reaches the bottom when its rect.bottom value is greater than or equal to the screen’s rect.bottom attribute
                # treat this the same as if the shhip got hit
                self._ship_hit()
                break

    def _check_play_button(self, mouse_pos):
        """start a new game when the player clicks play"""

        button_clicked = self.play_button.rect.collidepoint(
            mouse_pos
        )  # The flag button_clicked stores a True or False value
        if button_clicked and not self.stats.game_active:  # and the game will restart only if Play is clicked and the game is not currently active
            # reset the game settings
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()  # we reset the game statistics, which gives the player three new ships
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            # get rid of any remaining aliens and bullets
            self.aliens.empty()  # We empty the aliens and bullets groups
            self.bullets.empty()

            # create a new fleet and center the ship
            self._create_fleet()  # and then create a new fleet and center the ship
            self.ship.center_ship()
            pygame.mouse.set_visible(False)


if __name__ == "__main__":
    # make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
