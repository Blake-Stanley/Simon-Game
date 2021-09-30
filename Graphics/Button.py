#(c) A+ Computer Science
# www.apluscompsci.com

import pygame
from pygame.locals import *

# A pressable button
class Button:
    # Set up the button using the word to decide the size
    def __init__(self, newX, newY, word):
        self.x = newX
        self.y = newY
        self.font = pygame.font.Font(None, 25)
        size = self.font.size(word)
        self.height = size[1]+10
        self.width = size[0]+10
        self.text = word

    # Draw the button
    def draw(self, window):
        pygame.draw.rect(window, (166,254,0), (self.x-self.width/2, self.y-self.height/2, self.width,self.height))
        text = self.font.render(self.text,1, (0, 0, 0))
        textpos = text.get_rect(centerx=self.x, centery=self.y)
        window.blit(text, textpos)

    # Determine if the mouse click was on the button
    def isClicked(self,mouse):
        if(mouse[0] >= self.x-self.width/2 and mouse[0] <= self.x+self.width/2 
           and mouse[1] >= self.y - self.height/2 and mouse[1] <= self.y+self.height/2):
            return True
        return False
