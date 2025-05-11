import pygame as pg
from sprites import *
from modes.mode_obj import *
from sprites import sprites,Timer
import colors as col
import os
from time import sleep

ZONE_START = (100,100)
ZONE_MARGINS = (200,400)
ZONE_SIZE = (190, 395)

class Sandview:
    def __init__(self, screen : pg.Surface, mode : Mode, fps : int):
        self.screen = screen
        self.mode = mode
        self.fps = fps
        self.world_cards : list[list[pg.sprite.Sprite]] = []
        self.selected_world = 0
        self.move_timer = Timer(framerate=10)
    
    def frame(self):
        keys = pg.key.get_pressed()
        can_move = self.move_timer.tick()
        if keys[pg.K_LEFT] and can_move:
            self.selected_world = (self.selected_world - 1) % len(self.world_cards)
            self.select_world(self.selected_world)
        if keys[pg.K_RIGHT] and can_move:
            self.selected_world = (self.selected_world + 1) % len(self.world_cards)
            self.select_world(self.selected_world)
    
    def select_world(self, world_n : int):
        for i,world in enumerate(self.world_cards[:-1]):
            if i == world_n:
                world[0].color = col.selected
                world[1].select()
                world[2].ch_text(color=col.selected)
                world[3].ch_text(color=col.selected)
                world[4].ch_text(color=col.selected)
                world[5].ch_text(color=col.selected)
            else:
                world[0].color = col.borders
                world[1].unselect()
                world[2].ch_text(color=col.borders)
                world[3].ch_text(color=col.borders)
                world[4].ch_text(color=col.borders)
                world[5].ch_text(color=col.borders)

        if world_n == len(self.world_cards) - 1: self.world_cards[-1].select()
        else: self.world_cards[-1].unselect()

    def ch_mode_c(self : Self, mode : Mode):
        def __():
            self.mode.set_as(mode)
        return __

    def init(self):
        sprites.empty()
        modes = resolve_saves()
        for i,world in enumerate(modes):
            card_start_x = ZONE_START[0]+(i%9)*ZONE_MARGINS[0]
            card_start_y = ZONE_START[1]+(i//9)*ZONE_MARGINS[1]
            mode, max_score = world

            self.world_cards.append([
                add(Border(pg.Rect(card_start_x, card_start_y, *ZONE_SIZE),4)),
                add(Button(
                    pg.Rect(card_start_x+10, card_start_y + ZONE_SIZE[1] - 45, ZONE_SIZE[0] - 20, 40),
                    "Play",
                    self.ch_mode_c(mode),
                    border=4
                )),
                add(Text((card_start_x + 10, card_start_y + 50),
                         "Size Range:",
                         "small"
                )),
                add(Text((card_start_x + 10, card_start_y + 65),
                         f"{mode.gen_range[0]}-{mode.gen_range[1]}",
                         "small"
                )),
                add(Text((card_start_x + 10, card_start_y + 90),
                         f"Max Score:",
                         "small"
                )),
                add(Text((card_start_x + 10, card_start_y + 105),
                         f"{max_score}",
                         "small"
                )),
            ])
        
        card_start_x = ZONE_START[0]+(len(modes)%9)*ZONE_MARGINS[0]
        card_start_y = ZONE_START[1]+(len(modes)//9)*ZONE_MARGINS[1]

        self.world_cards.append(add(Button(
            pg.Rect(card_start_x, card_start_y, *ZONE_SIZE),
            "+",
            self.ch_mode_c(Mode("sandbox"))
        )))

        self.select_world(0)
        sleep(1/self.fps*10)
    
def resolve_saves():
    if not os.path.isfile("./save/sandbox.txt"): f = open("./save/sandbox.txt", "xr")
    else: f = open("./save/sandbox.txt", "r")
    with f as file: modes = file.read()
    modes = modes.split("\n")
    modes = [parse_world(i) for i in modes]
    return modes

def parse_world(world : str) -> Mode:
    gen_range,max_score = world.split(",")
    gen_range = tuple([int(i) for i in gen_range.split("-")])
    return (Mode("game").set_gen(gen_range), max_score)

def add(obj : pg.sprite.Sprite) -> pg.sprite.Sprite:
    sprites.add(obj)
    return obj