import pygame as pg
import os
import button 
import time

surface = pg.display.set_mode((672,672))
pg.display.set_caption("Simon Game")

screen = pg.display.set_mode((672,672))
mainPNG = pg.image.load("simondefault1.png")

pg.font.init()
#from button.py
buttonG = button.Button(0, 0, 335, 335, "Green")
buttonR = button.Button(335, 0, 672, 335, "Red")
buttonY = button.Button(0, 335, 335, 672, "Yellow")
buttonB = button.Button(335, 335, 672, 672, "Blue")

buttonG.draw(screen, 0, 200, 0)
buttonR.draw(screen, 200, 0 ,0)
buttonY.draw(screen, 200, 70 ,50)
buttonB.draw(screen, 0, 0 ,200)
screen.blit(mainPNG, (0, 0))
    
pg.display.flip()

#color must be inputted as 'r' 'g' 'b' or 'y'
def flash(color):
    if color == 'y':
        flashedPNG = pg.image.load("simonyellow1.png")
    elif color == 'b':
        flashedPNG = pg.image.load("simonblue1.png")
    elif color == 'r':
        flashedPNG = pg.image.load("simonred1.png")
    else: 
        flashedPNG = pg.image.load("simongreen1.png")  
    
    screen.blit(flashedPNG, (0,0))
    time.sleep(10)
    screen.blit(mainPNG, (0,0))

# variable tracks whether the button has been clicked so that if you hold down mouseclick it only clicks once 
allowClick = True
loop = True
currentColor = ''
while loop:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = False 
    pg.display.update() # delete this?
    if event.type == pg.MOUSEBUTTONDOWN and allowClick is True:
        allowClick = False
        pos = pg.mouse.get_pos()
        if buttonG.isClicked(pos):
            currentColor = 'g'
            #print("green")
            #flash('g')
            #print("through")
        elif buttonR.isClicked(pos):
            currentColor = 'r'
            #print("Red")
            #flash('r')
        elif buttonY.isClicked(pos):
            currentColor = 'y'
            #print("Yellow")
            #flash('y')
        elif buttonB.isClicked(pos):
            currentColor = 'b'
            #print("Blue")
            #flash('b')
        
    if event.type == pg.MOUSEBUTTONUP:
        if allowClick: # prevents this block from running multiple times
            pass
        else:
            print("up detected")
            print(currentColor)
            flash(currentColor)
            allowClick = True
         
 
pg.quit()
quit()


