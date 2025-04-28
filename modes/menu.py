import pygame as pg
from sprites import *
from utils import ModeLink

class Menu:
    def __init__(self, screen : pg.Surface, mode_link : ModeLink):
        self.screen = screen
        self.play_button = Button(pg.Rect(450,450,150,100),"Play", lambda: self.mode_link.set_mode("game"))
        buttons.add(self.play_button)
        self.mode_link = mode_link
    
    def frame(self):
        title_text = precompile_text(f"N-Tris","logo")
        self.screen.blit(title_text,(300,50))
        buttons.update(self.screen)
        pressed = pg.mouse.get_pressed()
        pos = pg.mouse.get_pos()
        if pressed[0]:
            [i.click_check(pos) for i in buttons]
    
    def draw(self):
        self.frame()