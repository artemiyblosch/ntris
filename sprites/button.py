import pygame as pg
from assets_lib.fonts import precompile_text
from types_ import Point

buttons = pg.sprite.Group()

class Button(pg.sprite.Sprite):
    def __init__(self, rect : pg.Rect, text : str, onClick, font : str = "default"):
        super().__init__()
        self.rect = rect
        self.text = text
        self.onClick = onClick
        self.font = font
    
    def click_check(self, pos : Point):
        if self.rect.collidepoint(pos):
            self.onClick()
    
    def update(self, screen : pg.Surface):
        pg.draw.rect(screen, (255,255,255), self.rect, 10, 2)

        text = precompile_text(self.text, self.font)
        rect = text.get_rect(center=self.rect.center)
        screen.blit(text, rect)