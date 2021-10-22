import pygame.font

class Button:

    def __init__(self,ai_game,msg): # 
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48) # prepare font attribute for rendering 

        #build the buttons rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height) #center the button on the screen, we create a rect for the button
        self.rect.center = self.screen_rect.center

        #the button message needs to be prepped only once
        self._prep_msg(msg) #Pygame works with text by rendering the string you want to display as an image. At y, we call _prep_msg() to handle this rendering.

    def _prep_msg(self,msg):
        """turn msg into a rendered image and center text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color) #The call to font.render() turns the text stored in msg into an image, which we then store in self.msg_image
        self.msg_image_rect = self.msg_image.get_rect() #At v, we center the text image on the button by creating a rect from the image and setting its center attribute to match that of the button
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        #draw blank button and then draw message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        
