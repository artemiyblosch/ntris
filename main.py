import pygame as pg
import sys
from map import *
from timing import Timer
from utils import *
from fonts import *
from generating import *
from time import sleep

pg.init()
screen = pg.display.set_mode((1000,1000))
clock = pg.time.Clock()

map = Map()
gen_range = (3,11)
gen_figure(map,size_range=gen_range)

fps = 60
score = 0

fall_timer = Timer(framerate=8)
move_timer = Timer(framerate=13)
rotate_timer = Timer(framerate=9)
pause_timer = Timer(framerate=3)

stun_cooldown = 0
zone_start = (110,4*32)
paused = False

load_font("default", (None,36))

while True:
    pg.draw.rect(screen,(0,0,0),(0,0,1000,1000))
    pg.draw.rect(screen,(111,111,111),(zone_start[0]-5,zone_start[1]-5,21*16 + 10,42*16 + 10),5)
    score_text = precompile_text(f"Score: {score}","default")
    screen.blit(score_text,(500,600))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    
    keys = pg.key.get_pressed()
    can_do = move_timer.tick(fps)

    if keys[pg.K_F1]:
        paused = not paused
        sleep(0.1)
    if paused: 
        pg.draw.rect(screen,(128,128,128),(0,0,1000,1000))
        continue

    if keys[pg.K_RIGHT] and map.can_move(direction=(1,0)) and can_do:
        map.move(direction=(1,0))
        stun_cooldown += 1
    if keys[pg.K_LEFT] and map.can_move(direction=(-1,0)) and can_do:
        map.move(direction=(-1,0))
        stun_cooldown += 1
    if keys[pg.K_DOWN] and map.can_move() and can_do:
        map.move()
        stun_cooldown = 20
    if keys[pg.K_UP] and map.can_rotate() and rotate_timer.tick():
        map.rotate()
        stun_cooldown += 1
    if keys[pg.K_v] and map.can_flip() and rotate_timer.tick():
        map.flip()
        stun_cooldown += 1
    
    
    for i,v in enum(map):
        if i[1] < 42: pg.draw.rect(screen, v.color,(i[0] * 16 + zone_start[0], 1000 - zone_start[1] - 6*16 + 8 - i[1] * 16,16,16))
    
    if map.can_move():
        if fall_timer.tick(fps): map.move()
        stun_cooldown = 20
    elif stun_cooldown < 0:
        map.remove_figure_status()
        gen_figure(map,size_range=gen_range)
        score += 1
        is_going = True
        while is_going:
            is_going = False
            for i in range(41):
                if not has(map.get_line(i),None):
                    score += 10 
                    map.delete_line(i)
                    is_going = True
    
    pg.display.flip()
    clock.tick(fps)
    stun_cooldown -= 1