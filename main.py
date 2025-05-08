import pygame as pg
import sys
from modes import *
from assets_lib.fonts import load_font

pg.init()
screen = pg.display.set_mode((1000,1000))
clock = pg.time.Clock()

gen_range = (3,10)
fps = 60
mode = ModeLink("menu")

game = Game(screen,mode,fps,gen_range)
menu = Menu(screen,mode)

load_font("default", ('./assets/fonts/ARCADECLASSIC.TTF',36))
load_font("big", ('./assets/fonts/ARCADECLASSIC.TTF',90))
load_font("logo", (None,200))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    screen.fill((12,12,12))
    if mode.mode == "game": game.frame()
    elif mode.mode == "menu": menu.frame()

    pg.display.flip()
    clock.tick(fps)