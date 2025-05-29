import pygame as pg
from sprites import *
from modes.mode_obj import *
from sprites import *
from layouts import Grid, ViewScreen_Layout
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
        self.go_back_button = Button(pg.Rect(10,10,30,30),"X", lambda: self.mode.set_mode("menu"),"small",2)
        self.view_grid = Grid(
            (ViewScreen_Layout(0.2),ViewScreen_Layout(0,0.4)),
            (ViewScreen_Layout(0.1),ViewScreen_Layout(0,0.025)),
            (ViewScreen_Layout(0.2),ViewScreen_Layout(0,0.1))
        )
    
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
        for i,world in enumerate(self.world_cards):
            if i == world_n: world.select()
            else: world.unselect()

    def ch_mode_c(self : Self, mode : Mode):
        def __():
            self.mode.set_as(mode)
        return __

    def init(self):
        sprites.empty()
        sprites.add(self.go_back_button)
        modes : list[tuple[Mode,int]] = resolve_saves()
        for i,world in enumerate(modes):
            self.world_cards.append(add(Card(world,self.view_grid[i%7,i//7],self.mode)))

        self.world_cards.append(add(Button(
            self.view_grid[len(modes)%7,len(modes)//7],
            "+",
            self.ch_mode_c(Mode("sandbox").set_sandbox(len(modes)))
        )))

        self.select_world(0)
        sleep(1/self.fps*10)
    
    def delete_entry_c(self, entry : int):
        def __():
            with open("./save/sandbox.txt", "r") as file: entries = file.read().split("\n")
            del entries[entry]
            with open("./save/sandbox.txt", "w") as file: file.write("\n".join(entries))
            self.world_cards = []
            self.init()
        return __
    
def resolve_saves():
    with open("./save/sandbox.txt", "r") as file: modes = file.read()
    if modes == "": return []
    
    modes = modes.split("\n")
    modes = [parse_world(v,i) for i,v in enumerate(modes) if v != ""]
    return modes

def parse_world(world : str, entry : int) -> tuple[Mode,int]:
    gen_range,max_score = world.split(",")
    gen_range = tuple([int(i) for i in gen_range.split("-")])
    return (Mode("game").set_gen(gen_range).set_sandbox(entry), max_score)

def add(obj : pg.sprite.Sprite) -> pg.sprite.Sprite:
    sprites.add(obj)
    return obj