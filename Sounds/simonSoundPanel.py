#Simon Sound Panel

import pygame
import pygame._sdl2 as sdl2
from pygame import *

#Inits the Mixer functions
pygame.init()
is_capture = 0  # zero to request playback devices, non-zero to request recording devices
num = sdl2.get_num_audio_devices(is_capture)
names = [str(sdl2.get_audio_device_name(i, is_capture), encoding="utf-8") for i in range(num)]
#print("\n".join(names))
deviceName = str(sdl2.get_audio_device_name(0, is_capture), encoding="utf-8")
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512, devicename= deviceName, allowedchanges=AUDIO_ALLOW_FREQUENCY_CHANGE | AUDIO_ALLOW_CHANNELS_CHANGE)

def soundColor(color):

    if(color == 'g'):
        #creates the sound object
        greenSound = pygame.mixer.Sound("Sounds/D_01.ogg")

        #plays the sound object
        pygame.mixer.Sound.play(greenSound, maxtime = 400)


    if(color == 'r'):
        #creates the sound object
        redSound = pygame.mixer.Sound("Sounds/F_01.ogg")

        #plays the sound object
        pygame.mixer.Sound.play(redSound, maxtime = 400)


    if(color == 'y'):
        #creates the sound object
        yellowSound = pygame.mixer.Sound("Sounds/A_01.ogg")

        #plays the sound object
        pygame.mixer.Sound.play(yellowSound, maxtime = 400)


    if(color == 'b'):
        #creates the sound object
        blueSound = pygame.mixer.Sound("Sounds/C_01.ogg")

        #plays the sound object
        pygame.mixer.Sound.play(blueSound, maxtime = 400)

