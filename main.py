import pygame as pg
import button
import simonSoundPanel
import logic

surface = pg.display.set_mode((672, 672))
pg.display.set_caption("Simon Game")

screen = pg.display.set_mode((672, 672))
mainPNG = pg.image.load("simondefault1.png")

pg.font.init()
# from button.py
buttonG = button.Button(0, 0, 335, 335, "Green")
buttonR = button.Button(335, 0, 672, 335, "Red")
buttonY = button.Button(0, 335, 335, 672, "Yellow")
buttonB = button.Button(335, 335, 672, 672, "Blue")

buttonG.draw(screen, 0, 200, 0)
buttonR.draw(screen, 200, 0, 0)
buttonY.draw(screen, 200, 70, 50)
buttonB.draw(screen, 0, 0, 200)
screen.blit(mainPNG, (0, 0))

pg.display.flip()

# color must be inputted as 'r' 'g' 'b' or 'y'
y = pg.image.load("simonyellow1.png")
b = pg.image.load("simonblue1.png")
r = pg.image.load("simonred1.png")
g = pg.image.load("simongreen1.png")


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
    pg.display.update()
    pg.time.delay(200)
    screen.blit(mainPNG, (0, 0))
    pg.display.update()
    # print("flash")


# runs computer sequence
def runSequence():
    pg.time.delay(500)
    for i in range(len(logic.getSequence())):
        flash(logic.getSequence()[i])
        simonSoundPanel.soundColor(logic.getSequence()[i])
        pg.time.delay(300)


# add value to sequence to create first sequence
logic.progress()
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
            print("you failed")  # bring to lose screen instead
            loop = False
        print("iterated")

        if len(logic.getPlayerSequence()) == len(logic.getSequence()):
            logic.clearPlayerSequence()
            logic.progress()
            runSequence()
            print("running sequence")
        allowClick = True


pg.quit()
quit()