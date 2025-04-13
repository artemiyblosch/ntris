import pygame as pg
import sys
from map import Map, enum
import random

pg.init()
screen = pg.display.set_mode((800,800))
clock = pg.time.Clock()

map = Map()
map.gen_figure(size=random.randint(1,12))

while True:
    pg.draw.rect(screen,(0,0,0),(0,0,800,800))
    pg.draw.rect(screen,(111,111,111),(110,4*32,11*32,21*32),5)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    
    keys = pg.key.get_pressed()
    if keys[pg.K_RIGHT]:
        print("Нажата клавиша enter")
    
    for i,v in enum(map):
        if i[1] < 21: pg.draw.rect(screen, v.color,(i[0] * 32 + 110, 24*32 - i[1] * 32,32,32))
    
    if map.can_fall():
        map.fall()
    else:
        map.remove_figure_status()
        map.gen_figure(size=random.randint(1,12))
    
    pg.display.flip()
    clock.tick(10)