import pygame as pg
from sprites import *
from modes.mode_obj import Mode
from sprites import sprites
from layouts import Grid, ViewScreen_Layout, supports_layouts

@supports_layouts
class Menu:
    def __init__(self, screen : pg.Surface, mode : Mode):
        self.screen = screen
        self.play_button = Button(
            (Grid(
                (260,100),
                (0,0),
                (ViewScreen_Layout(0.5,offset=-130),ViewScreen_Layout(0,0.5,-130))
            ),(0,0)),
            "Sandbox",
            lambda: self.mode.set_mode("wview")
        )
        self.play_button.selected = True
        self.mode = mode
        self.logo_y = ViewScreen_Layout(0,0.1)
        self.logo_x = ViewScreen_Layout(0.5,offset=-150)
    
    def init(self):
        sprites.empty()
        sprites.add(self.play_button)

    def frame(self):
        draw_on(self.screen, get_image("logo.png",True),(self.logo_x,self.logo_y))
    
    def draw(self):
        self.frame()
    