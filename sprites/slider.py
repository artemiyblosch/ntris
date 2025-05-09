import pygame as pg
from types_ import Point
from utils import closest

sliders = pg.sprite.Group()

class Slider(pg.sprite.Sprite):
    def __init__(self, pos : Point, width : int, values : range, init_value : int):
        super().__init__()
        self.pos = pos
        self.width = width
        self.values = values
        self.value = init_value
        sliders.add(self)
    
    def update(self, screen : pg.Surface):
        pg.draw.rect(screen, (255,255,255), (*self.pos, self.width, 8),2)
        pg.draw.rect(screen, (255,255,255), self.get_selector_rect())
    
    def get_selector_rect(self):
        return pg.Rect( self.v2x(self.value), self.pos[1] - 4, 16, 16 )
    
    def click_check(self, pos : Point):
        if pg.Rect(self.pos[0] - 8, self.pos[1] - 8, self.width + 8, 16).collidepoint(pos):
            self.value = closest(self.values,self.x2v(pos[0]))
    
    def v2x(self, value : int) -> int:
        delta = (self.values.stop - self.values.start) / self.values.step
        amount = value - self.values.start
        return (self.pos[0]-8) + amount*(self.width / delta)

    def x2v(self, x : int) -> int:
        delta = (self.values.stop - self.values.start) / self.values.step
        return ( x - (self.pos[0]-8) ) / (self.width / delta) + self.values.start