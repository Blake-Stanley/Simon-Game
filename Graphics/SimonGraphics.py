import pygame as pg
import os
 

screen = pg.display.set_mode((672,672))
sprite = pg.image.load("simondefault1.png")


loop = True
while loop:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			loop = False
	screen.blit(sprite, (0, 0))
	pg.display.flip()

	if event.type == pg.KEYDOWN:
		print("clicked")

pg.quit()
