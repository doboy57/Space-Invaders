class Settings:
    def __init__(self):
        """Initialize the settings."""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 7
        self.ship_limit = 3
        # bullet settings
        self.bullet_speed = 10
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 20 
        #alien settings
        self.alien_speed = 1.5
        self.fleet_drop_speed = 8
        # How quickly the game speeds up
        self.speedup_scale = 1.1 # At u, we add a speedup_scale setting to control how quickly the game speeds up:
        #how quickly the alien point values increase 
        self.score_scale = 1.5 # how quickly the alien point values increase
        self.initialize_dynamic_settings() #Finally, we call the initialize_dynamic_settings() method to initialize the values for attributes that need to change throughout the game
        # fleet_direction of 1 represents right -1 represents left
        self.fleet_direction = 1
    def initialize_dynamic_settings(self):
        """initialize settings that change throughout the game"""
        self.ship_speed = 4
        self.bullet_speed = 5
        self.alien_speed = 1

        # fleet_direction of 1 represents right: -1 represents left
        self.fleet_direction = 1
        # scoring 
        self.alien_points = 50
    
    def increase_speed(self):
        """increase speed settings and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale) #Now when we increase the game’s speed, we also increase the point value of each hit
        