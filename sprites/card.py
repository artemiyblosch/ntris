import pygame as pg

from sprites.button import *
from sprites.border import *
from sprites.text import *

from modes.mode_obj import Mode
from layouts import Rect_Layout


class Card(pg.sprite.Sprite):
    def __init__(self, world : tuple[Mode,int], rect : Rect_Layout, mode_link):
        super().__init__()
        self.world = world
        self.mode_link = mode_link
        self.card_left, self.card_top, self.card_width, self.card_height = rect

        self.card_sprites = pg.sprite.Group()
        self.border = self.add(Border(rect,4))
        self.sr_text = self.add(Text((self.card_top + 10, self.card_left + 50),
                         "Size Range:",
                         "small"
                ))
        self.sra_text = self.add(Text((self.card_top + 10, self.card_left + 65),
                         f"{self.world[0].gen_range[0]}-{self.world[0].gen_range[1]}",
                         "small"
                ))
        self.max_text = self.add(Text((self.card_top + 10, self.card_left + 90),
                         f"Max Score:",
                         "small"
                ))
        self.score_text = self.add(Text((self.card_top + 10, self.card_left + 105),
                         f"{self.world[1]}",
                         "small"
                ))
        self.del_button = self.add(Button(
                    Rect_Layout(self.card_top + 10, self.card_top+self.card_height - 90, self.card_width - 20, 40),
                    "Delete",
                    self.delete_entry_c(self.world[0].sandbox_entry),
                    border=4
                ))
        self.play_button = self.add(Button(
                    Rect_Layout(self.card_top + 10, self.card_top+self.card_height - 90, self.card_width - 20, 40),
                    "Delete",
                    self.delete_entry_c(self.world[0].sandbox_entry),
                    border=4
                ))
    
    def update(self,screen):
        self.card_sprites.update(screen)

    def delete_entry_c(self, entry : int):
        def __():
            with open("./save/sandbox.txt", "r") as file: entries = file.read().split("\n")
            del entries[entry]
            with open("./save/sandbox.txt", "w") as file: file.write("\n".join(entries))
            self.world_cards = []
            self.init()
        return __

    def add(self,obj : pg.sprite.Sprite) -> pg.sprite.Sprite:
        self.card_sprites.add(obj)
        return obj
    
    def select(self):
        self.border.color = col.selected
        self.sr_text.ch_text(color=col.selected)
        self.sra_text.ch_text(color=col.selected)
        self.score_text.ch_text(color=col.selected)
        self.max_text.ch_text(color=col.selected)
    
    def unselect(self):
        self.border.color = col.borders
        self.sr_text.ch_text(color=col.borders)
        self.sra_text.ch_text(color=col.borders)
        self.score_text.ch_text(color=col.borders)
        self.max_text.ch_text(color=col.borders)
    
    def click_check(self, pos): pass