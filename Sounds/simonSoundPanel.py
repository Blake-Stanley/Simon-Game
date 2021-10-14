#Simon Sound Panel

import pygame
from pygame import *

#Inits the Mixer functions
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512, devicename= "Built-in Output", allowedchanges=AUDIO_ALLOW_FREQUENCY_CHANGE | AUDIO_ALLOW_CHANNELS_CHANGE)

def soundColor(color):

    if(color == 'g'):
        #creates the sound object
        greenSound = pygame.mixer.Sound("D_01.ogg")

        #plays the sound object
        pygame.mixer.Sound.play(greenSound, maxtime = 400)


    if(color == 'r'):
        #creates the sound object
        redSound = pygame.mixer.Sound("F_01.ogg")

        #plays the sound object
        pygame.mixer.Sound.play(redSound, maxtime = 400)


    if(color == 'y'):
        #creates the sound object
        yellowSound = pygame.mixer.Sound("A_01.ogg")

        #plays the sound object
        pygame.mixer.Sound.play(yellowSound, maxtime = 400)


    if(color == 'b'):
        #creates the sound object
        blueSound = pygame.mixer.Sound("C_01.ogg")

        #plays the sound object
        pygame.mixer.Sound.play(blueSound, maxtime = 400)
