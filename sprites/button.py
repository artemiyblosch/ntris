import pygame as pg
from sprites.fonts import precompile_text
from types_ import Point

buttons = pg.sprite.Group()

class Button(pg.sprite.Sprite):
    def __init__(self, rect : pg.Rect, text : str, onClick):
        super().__init__()
        self.rect = rect
        self.text = text
        self.onClick = onClick
    
    def click_check(self, pos : Point):
        if self.rect.collidepoint(pos):
            self.onClick()
    
    def update(self, screen : pg.Surface):
        pg.draw.rect(screen,(255,255,255),self.rect,10,2)
        text = precompile_text(self.text,"default")
        screen.blit(text,self.rect)