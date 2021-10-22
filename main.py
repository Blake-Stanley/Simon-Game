import pygame as pg

# by including a "__init__.py" in all the folders, by doing folder.file we can import from other folders
import Graphics.Button as button
import Sounds.simonSoundPanel as simonSoundPanel
import Logic.logic as logic

surface = pg.display.set_mode((672, 672))
pg.display.set_caption("Simon Game")

screen = pg.display.set_mode((672, 672))
mainPNG = pg.image.load("Graphics/simondefault1.png")

pg.init()
font = pg.font.Font('freesansbold.ttf', 32)

# create buttons that rest behind pngs that create clickability
buttonG = button.Button(0, 0, 335, 335, "Green")
buttonR = button.Button(335, 0, 672, 335, "Red")
buttonY = button.Button(0, 335, 335, 672, "Yellow")
buttonB = button.Button(335, 335, 672, 672, "Blue")

pg.display.flip()

# color must be inputted as 'r' 'g' 'b' or 'y'
# loading in game pngs
y = pg.image.load("Graphics/simonyellow1.png")
b = pg.image.load("Graphics/simonblue1.png")
r = pg.image.load("Graphics/simonred1.png")
g = pg.image.load("Graphics/simongreen1.png")



def flash(color):
    if color == "y":
        flashedPNG = y
    elif color == "b":
        flashedPNG = b
    elif color == "r":
        flashedPNG = r
    else:
        flashedPNG = g

    screen.blit(flashedPNG, (0, 0))

    highScore = logic.getHighScore()
    
    # putting high score on the screen
    text2 = font.render(f"Best: {highScore}", True, (50, 250, 50))
    textRect2 = text2.get_rect()
    textRect2.center = ((672 / 6 + 4) * 5 -5, 640)
    surface.blit(text2, textRect2)

    # putting current score on the screen
    text = font.render(f"Score: {len(logic.getSequence()) - 1}", True,
                       (50, 250, 50))
    textRect = text.get_rect()
    textRect.center = (672 / 6 - 20, 640)
    surface.blit(text, textRect)

    pg.display.update()

    pg.time.delay(200)
    screen.blit(mainPNG, (0, 0))
    surface.blit(text, textRect)
    surface.blit(text2, textRect2)

    pg.display.update()


# runs computer sequence of pattern user copies
def runSequence():
    pg.time.delay(700)
    for i in range(len(logic.getSequence())):
        flash(logic.getSequence()[i])
        simonSoundPanel.soundColor(logic.getSequence()[i])
        pg.time.delay(300)


# runs the actual game
def mainGame():
    buttonG.draw(screen, 0, 200, 0)
    buttonR.draw(screen, 200, 0, 0)
    buttonY.draw(screen, 200, 70, 50)
    buttonB.draw(screen, 0, 0, 200)
    screen.blit(mainPNG, (0, 0))
    
    highScore = logic.getHighScore()
    
    # add value to sequence to create first sequence
    logic.progress()
    # putting high score on the screen
    text2 = font.render(f"Best: {highScore}", True, (50, 250, 50))
    textRect2 = text2.get_rect()
    textRect2.center = ((672 / 6 + 4) * 5 -5, 640)
    surface.blit(text2, textRect2)

    # putting current score on the screen
    text = font.render(f"Score: {len(logic.getSequence()) - 1}", True,
                       (50, 250, 50))
    textRect = text.get_rect()
    textRect.center = (672 / 6 - 20, 640)
    surface.blit(text, textRect)
    pg.display.update()
    pg.time.delay(300)
    
    runSequence()

    # variable tracks whether the button has been clicked so that if you hold down mouseclick it only clicks once
    allowClick = True
    loop = True
    currentColor = ""
    while loop:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                loop = False

            if event.type == pg.MOUSEBUTTONDOWN and allowClick is True:
                allowClick = False
                pos = pg.mouse.get_pos()
                if buttonG.isClicked(pos):
                    currentColor = "g"
                elif buttonR.isClicked(pos):
                    currentColor = "r"
                elif buttonY.isClicked(pos):
                    currentColor = "y"
                elif buttonB.isClicked(pos):
                    currentColor = "b"

            if event.type == pg.MOUSEBUTTONUP and not allowClick:
                flash(currentColor)
                simonSoundPanel.soundColor(currentColor)
                logic.appendPlayerSequence(currentColor)
                if logic.check() is False:
                    loop = False
                    gameOver()

                elif len(logic.getPlayerSequence()) == len(logic.getSequence()):
                    logic.clearPlayerSequence()
                    logic.progress()
                    runSequence()
                allowClick = True



# loads in the title screen pngs
title1 = pg.image.load("Graphics/KGD Logo frame 1-1.png.png")
title2 = pg.image.load("Graphics/kgd frame 2.png")
title3 = pg.image.load("Graphics/kgd frame 3.png")
title4 = pg.image.load("Graphics/kgd frame 4.png")
title5 = pg.image.load("Graphics/kgd frame 5.png")

titles = [title1, title2, title3, title4, title5]
# title screen background png
background = pg.image.load("Graphics/background2.png")


# plays title screen animation
def titleScreen():
    screen.blit(background, (0, 0))  # upload background
    for title in titles:
        screen.blit(title, (0, 0))
        pg.display.update()
        pg.time.delay(200)
    titles.reverse()
    for title in titles:
        screen.blit(title, (0, 0))
        pg.display.update()
        pg.time.delay(200)

# menu screen to click play
menuScreen = pg.image.load("Graphics/titlescreen.png")
def menu():
    loop = True
    buttonStart = button.Button(170, 350, 370, 250, "Start")
    
    buttonStart.draw(surface, 255,255,255)
    screen.blit(menuScreen, (0, 0))
    pg.display.update()
        
    while loop:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                loop = False
                pg.quit()
                quit()
        
            if event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                if buttonStart.isClicked(pos):
                    loop = False
    mainGame()  
     

# screen to show score of the game, high score, and to be able to play again                
# lossScreen = pg.image.load("Graphics/titlescreen.png")
def lossPage():
    loop = True
    buttonReplay = button.Button(170, 350, 370, 250, "replay")
    
    buttonReplay.draw(surface, 255,255,255)
    # screen.blit(lossScreen, (0, 0))
    pg.display.update()
        
    while loop:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                loop = False
                pg.quit()
                quit()
        
            if event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                if buttonReplay.isClicked(pos):
                    loop = False
    mainGame() 

# clears data of current game, saving new high score if its higher and starts new game 
def gameOver():
    logic.setHighScore()
    logic.clearPlayerSequence()
    logic.clearSequence()
    lossPage()

# main function
def main():
    titleScreen()
    menu()


if __name__ == "__main__":
    main()
