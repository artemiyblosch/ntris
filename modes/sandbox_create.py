import pygame as pg
from sprites import *
from types_ import ModeLink

class Sandbox:
    def __init__(self, screen : pg.Surface, mode_link : ModeLink, fps : int):
        self.screen = screen
        self.mode_link = mode_link
        self.gen_slideA = Slider((200,200),200,range(3,20,1),4)
        self.fps = fps
    
    def frame(self):
        sliders.update(self.screen)
        pressed = pg.mouse.get_pressed()
        pos = pg.mouse.get_pos()
        if pressed[0]:
            [i.click_check(pos) for i in sliders]
    
    def draw(self):
        self.frame()