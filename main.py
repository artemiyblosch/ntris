import pygame as pg
import sys
from modes import *
from assets_lib.fonts import load_font

def mode_obj(mode : Mode):
    if mode.mode == "sandbox": return sandbox
    if mode.mode == "menu": return menu
    if mode.mode == "game": return game

pg.init()
screen = pg.display.set_mode((1000,1000))
clock = pg.time.Clock()
select_timer = Timer(framerate=9)

gen_range = (3,10)
fps = 60
mode = Mode("menu")

game = Game(screen,mode,fps)
menu = Menu(screen,mode)
sandbox = Sandbox(screen,mode,fps)

load_font("small", ('./assets/fonts/ARCADECLASSIC.TTF',16))
load_font("default", ('./assets/fonts/ARCADECLASSIC.TTF',36))
load_font("big", ('./assets/fonts/ARCADECLASSIC.TTF',90))
load_font("giant", ('./assets/fonts/ARCADECLASSIC.TTF',160))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    screen.fill((12,12,12))

    if mode.init and mode.mode == "game":
        game = Game(screen,mode,fps)
    if mode.init:
        mode.init = False
        mode_obj(mode).init()

    sprites.update(screen)
    pressed = pg.mouse.get_pressed()
    pos = pg.mouse.get_pos()
    if pressed[0]:
        [i.click_check(pos) for i in sprites]
    
    mode_obj(mode).frame()

    keys = pg.key.get_pressed()
    if keys[pg.K_RETURN] and select_timer.tick(fps): Button.selected_callback()

    pg.display.flip()
    clock.tick(fps)