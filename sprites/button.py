import pygame as pg
from assets_lib.fonts import precompile_text
from types_ import Point
from sprites.all import sprites

class Button(pg.sprite.Sprite):
    def __init__(self, rect : pg.Rect, text : str, onClick, font : str = "default", border : int = 10):
        super().__init__()
        self.rect = rect
        self.text = text
        self.onClick = onClick
        self.font = font
        self.selected = False
        self.border = border
    
    def click_check(self, pos : Point):
        if self.rect.collidepoint(pos):
            self.onClick()
    
    def select(self):
        self.selected = True
        return self

    def update(self, screen : pg.Surface):
        pg.draw.rect(screen, (255,255,255), self.rect, self.border, 2)

        text = precompile_text(self.text, self.font)
        rect = text.get_rect(center=self.rect.center)
        screen.blit(text, rect)

    @staticmethod
    def selected_callback():
        for i in sprites:
            if isinstance(i,Button) and i.selected: i.onClick()