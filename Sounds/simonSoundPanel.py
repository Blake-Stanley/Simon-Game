#Simon Sound Panel

import pygame
from pygame import *

#Inits the Mixer functions
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512, devicename= "Built-in Output", allowedchanges=AUDIO_ALLOW_FREQUENCY_CHANGE | AUDIO_ALLOW_CHANNELS_CHANGE)

def soundGreen():

    #creates the sound object
    greenSound = pygame.mixer.Sound("D_01.ogg")

    #plays tge sound object
    pygame.mixer.Sound.play(greenSound)

def soundRed():

    #creates the sound object
    redSound = pygame.mixer.Sound("F_01.ogg")

    #plays tge sound object
    pygame.mixer.Sound.play(redSound)

def soundYellow():

    #creates the sound object
    yellowSound = pygame.mixer.Sound("A_01.ogg")

    #plays tge sound object
    pygame.mixer.Sound.play(yellowSound)

def soundBlue():

    #creates the sound object
    blueSound = pygame.mixer.Sound("C_01.ogg")

    #plays tge sound object
    pygame.mixer.Sound.play(blueSound)
