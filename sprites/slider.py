import pygame as pg
from types_ import Point
from utils import closest
from assets_lib import precompile_text, draw_on, get_image
import colors as col

class Slider(pg.sprite.Sprite):
    def __init__(self, pos : Point, width : int, values : range, init_value : int):
        super().__init__()
        self.pos = pos
        self.width = width
        self.values = range(values.start,values.stop+1,values.step)
        self.value = init_value
    
    def update(self, screen : pg.Surface):
        pg.draw.rect(screen, col.borders, (*self.pos, self.width, 8),2)
        draw_on(screen,get_image("slider_h.jpg"),self.get_selector_rect().topleft)

        start = precompile_text(str(self.values.start), "small", col.borders)
        s_rect = start.get_rect(center=(self.pos[0], self.pos[1] + 25))
        screen.blit(start,s_rect)

        end = precompile_text(str(self.values.stop - 1), "small", col.borders)
        e_rect = start.get_rect(center=(self.pos[0] - 8 + self.width, self.pos[1] + 25))
        screen.blit(end,e_rect)

        value = precompile_text(str(self.value), "small", (255,255,255))
        v_rect = start.get_rect(center=(self.pos[0] - 8 + self.width / 2, self.pos[1] - 25))
        screen.blit(value,v_rect)
    
    def get_selector_rect(self):
        return pg.Rect( self.v2x(self.value), self.pos[1] - 4, 16, 16 )
    
    def click_check(self, pos : Point):
        if pg.Rect(self.pos[0] - 40, self.pos[1] - 20, self.width + 80, 48).collidepoint(pos):
            self.value = closest(self.values,self.x2v(pos[0]))
    
    def v2x(self, value : int) -> int:
        delta = (self.values.stop - 1 - self.values.start) / self.values.step
        amount = value - self.values.start
        return (self.pos[0]-8) + amount*(self.width / delta)

    def x2v(self, x : int) -> int:
        delta = (self.values.stop - 1 - self.values.start) / self.values.step
        return ( x - (self.pos[0]-8) ) / (self.width / delta) + self.values.start