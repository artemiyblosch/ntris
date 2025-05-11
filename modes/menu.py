import pygame as pg
from sprites import *
from modes.mode_obj import Mode
from sprites import sprites

class Menu:
    def __init__(self, screen : pg.Surface, mode : Mode):
        self.screen = screen
        self.play_button = Button(\
            pg.Rect(350,450,250,100),\
            "Sandbox",\
            lambda: self.mode.set_mode("wview")\
        )
        self.play_button.selected = True
        self.mode = mode
    
    def init(self):
        sprites.empty()
        sprites.add(self.play_button)

    def frame(self):
        draw_on(self.screen, get_image("logo.png",True),(300,100))
    
    def draw(self):
        self.frame()