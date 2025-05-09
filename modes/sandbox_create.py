import pygame as pg
from sprites import *
from modes.mode_obj import *
from sprites import sprites

class Sandbox:
    def __init__(self, screen : pg.Surface, mode : Mode, fps : int):
        self.screen = screen
        self.mode = mode
        self.gen_slideA = Slider((200,400),200,range(3,21,1),4)
        self.gen_slideB = Slider((200,450),200,range(3,21,1),10)
        self.play_button = Button(\
            pg.Rect(350,700,250,100),\
            "Play",\
            lambda: self.mode.set_mode("game").set_gen((self.gen_slideA.value,self.gen_slideB.value))\
        ).select()
        self.fps = fps
    
    def init(self):
        sprites.empty()
        sprites.add(self.gen_slideA)
        sprites.add(self.gen_slideB)
        sprites.add(self.play_button)

    def frame(self):
        draw_on(self.screen, precompile_text("Size Range", "default"),(200,300))
    
    def draw(self):
        self.frame()