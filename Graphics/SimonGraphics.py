import pygame as pg
import os
import button 
import time

surface = pg.display.set_mode((672,672))

screen = pg.display.set_mode((672,672))
sprite = pg.image.load("simondefault1.png")

pg.font.init()
#from button.py
buttonG = button.Button(0, 0, 335, 335, "Green")
buttonR = button.Button(335, 0, 672, 335, "Red")
buttonY = button.Button(0, 335, 335, 672, "Yellow")
buttonB = button.Button(335, 335, 672, 672, "Blue")

# variable tracks whether the button has been clicked so that if you hold down mouseclick it only clicks once 
allowClick = True
loop = True
while loop:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = False
    buttonG.draw(screen, 0, 200, 0)
    buttonR.draw(screen, 200, 0 ,0)
    buttonY.draw(screen, 200, 70 ,50)
    buttonB.draw(screen, 0, 0 ,200)
    screen.blit(sprite, (0, 0))
    
    pg.display.flip()
    
    pg.display.update()
    if event.type == pg.MOUSEBUTTONDOWN and allowClick is True:
        allowClick = False
        pos = pg.mouse.get_pos()
        if buttonG.isClicked(pos):
            print("green")
        elif buttonR.isClicked(pos):
            print("Red")
        elif buttonY.isClicked(pos):
            print("Yellow")
        if buttonB.isClicked(pos):
            print("Blue")
    
    if event.type == pg.MOUSEBUTTONUP:
        allowClick = True
    
pg.quit()
quit()
