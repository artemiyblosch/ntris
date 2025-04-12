import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((800,800))
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    
    keys = pg.key.get_pressed()
    if keys[pg.K_RETURN]:
        print("Нажата клавиша enter")
    
    pg.display.flip()
    clock.tick(10)