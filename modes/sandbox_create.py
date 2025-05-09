import pygame as pg
from sprites import *
from types_ import ModeLink

class Sandbox:
    def __init__(self, screen : pg.Surface, mode_link : ModeLink, fps : int):
        self.screen = screen
        self.mode_link = mode_link
    
    def frame(self):
        title_text = precompile_text(f"N-Tris","logo")
        self.screen.blit(title_text,(300,50))
        buttons.update(self.screen)
        pressed = pg.mouse.get_pressed()
        pos = pg.mouse.get_pos()
        if pressed[0]:
            [i.click_check(pos) for i in buttons]
        
        keys = pg.key.get_pressed()

        if keys[pg.K_RETURN]: Button.selected_callback()
    
    def draw(self):
        self.frame()