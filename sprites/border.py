import pygame as pg
import colors as col
from types_ import Point

class Border(pg.sprite.Sprite):
    def __init__(self, rect : pg.Rect, border : int = 10, color : pg.Color = col.borders):
        super().__init__()
        self.rect = rect
        self.color = color
        self.border = border
    
    def update(self, screen : pg.Surface):
        pg.draw.rect(screen,self.color,self.rect,self.border)
    
    def click_check(self, pos : Point):
        pass