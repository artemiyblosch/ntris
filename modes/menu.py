import pygame as pg
from sprites import *
from types_ import ModeLink

class Menu:
    def __init__(self, screen : pg.Surface, mode_link : ModeLink):
        self.screen = screen
        self.play_button = Button(pg.Rect(350,450,250,100),"Sandbox", lambda: self.mode_link.set_ref("sandbox"))
        self.play_button.selected = True
        self.mode_link = mode_link
    
    def frame(self):
        draw_on(self.screen, get_image("logo.png",True),(300,100))
        buttons.update(self.screen)
        pressed = pg.mouse.get_pressed()
        pos = pg.mouse.get_pos()
        if pressed[0]:
            [i.click_check(pos) for i in buttons]
        
        keys = pg.key.get_pressed()

        if keys[pg.K_RETURN]: Button.selected_callback()
    
    def draw(self):
        self.frame()