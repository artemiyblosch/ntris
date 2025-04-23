import pygame as pg
import sys
from modes import *

pg.init()
screen = pg.display.set_mode((1000,1000))
clock = pg.time.Clock()

gen_range = (3,11)
fps = 60
mode = "menu"

game = Game(screen,fps,gen_range)

load_font("default", (None,36))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    game.frame()

    pg.display.flip()
    clock.tick(fps)