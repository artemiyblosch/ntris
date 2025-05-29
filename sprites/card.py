import pygame as pg

from sprites.button import *
from sprites.border import *
from sprites.text import *

from modes.mode_obj import Mode
from layouts import Rect_Layout


class Card(pg.sprite.Sprite):
    def __init__(self, world : tuple[Mode,int], rect : Rect_Layout,  play_c, del_c):
        super().__init__()
        self.world = world
        self.play_c = play_c
        self.del_c = del_c
        self.card_left, self.card_top, self.card_width, self.card_height = rect
        self.card_sprites = pg.sprite.Group()
        self.border = self.add(Border(rect,4))
        self.sr_text = self.add(Text((self.card_left + 10, self.card_top + 50),
                         "Size Range:",
                         "small"
                ))
        self.play_button = self.add(Button(
                    Rect_Layout(self.card_left + 10, self.card_top+self.card_height - 45, self.card_width - 20, 40),
                    "Play",
                    self.play_c,
                    border=4
                )),
        self.sra_text = self.add(Text((self.card_left + 10, self.card_top + 65),
                         f"{self.world[0].gen_range[0]}-{self.world[0].gen_range[1]}",
                         "small"
                ))
        self.max_text = self.add(Text((self.card_left + 10, self.card_top + 90),
                         f"Max Score:",
                         "small"
                ))
        self.score_text = self.add(Text((self.card_left + 10, self.card_top + 105),
                         f"{self.world[1]}",
                         "small"
                ))
        self.del_button = self.add(Button(
                    Rect_Layout(self.card_left + 10, self.card_top+self.card_height - 90, self.card_width - 20, 40),
                    "Delete",
                    self.del_c,
                    border=4
                ))
    
    def update(self,screen):
        self.card_sprites.update(screen)

    def add(self,obj : pg.sprite.Sprite) -> pg.sprite.Sprite:
        self.card_sprites.add(obj)
        return obj
    
    def select(self):
        self.border.color = col.selected
        self.sr_text.ch_text(color=col.selected)
        self.sra_text.ch_text(color=col.selected)
        self.score_text.ch_text(color=col.selected)
        self.max_text.ch_text(color=col.selected)
        self.play_button[0].select()
    
    def unselect(self):
        self.border.color = col.borders
        self.sr_text.ch_text(color=col.borders)
        self.sra_text.ch_text(color=col.borders)
        self.score_text.ch_text(color=col.borders)
        self.max_text.ch_text(color=col.borders)
        self.play_button[0].unselect()
    
    def click_check(self, pos): pass