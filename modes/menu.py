import pygame as pg
from sprites import *

class Menu:
    def __init__(self, screen : pg.Surface):
        self.screen = screen
        self.play_button = Button()

    def frame(self):
        title_text = precompile_text(f"N-Tris","default")
        self.screen.blit(title_text,(500,200))
        