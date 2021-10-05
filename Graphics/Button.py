import pygame
from pygame.locals import *

# A pressable button
class Button:
    # Set up the button using the word to decide the size
    def __init__(self, x1, y1, x2, y2, word):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.font = pygame.font.Font(None, 25)
        size = self.font.size(word)
        #self.height = size[1]+10
        #self.width = size[0]+10
        self.text = word
        #pygame.font.init()

    # Draw the button
    def draw(self, window, R, G, B):
        pygame.draw.rect(window, (R,G,B), (self.x1, self.y1, self.x2, self.y2))
        text = self.font.render(self.text,1, (0, 0, 0))
        textpos = text.get_rect(centerx=((self.x1+self.x2)/2), centery=((self.y1+self.y2)/2))
        window.blit(text, textpos)

    # Determine if the mouse click was on the button
    def isClicked(self,mouse):
        #print("mx = " , mouse[0], "\nmy = ", mouse[1])
        if(mouse[0] >= self.x1 and mouse[0] <= self.x2) and (mouse[1] >= self.y1 and mouse[1] <= self.y2):
            return True
        return False
