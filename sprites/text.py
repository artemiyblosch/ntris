import pygame as pg
import colors as col
from types_ import Point
from assets_lib import precompile_text, draw_on

class Text(pg.sprite.Sprite):
    def __init__(self, at : Point, text : str, font : str = "default", color : pg.Color = col.borders):
        super().__init__()
        self.text = text
        self.color = color
        self.font = font
        self.at = at
        self.text_image = precompile_text(self.text, self.font, self.color)
    
    def update(self, screen : pg.Surface):
        draw_on(screen, self.text_image,self.at)
    
    def click_check(self, pos : Point):
        pass

    def ch_text(self, text : str = None, font : str = None, color : pg.Color = None):
        if text == None: text = self.text
        if font == None: font = self.font
        if color == None: color = self.color
        self.text_image = precompile_text(text, font, color)