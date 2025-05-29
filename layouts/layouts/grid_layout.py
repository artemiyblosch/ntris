from types_ import Point
from pygame import Rect
from layouts.decor.layouty import supports_layouts
from layouts.layouts.rect_layout import Rect_Layout

@supports_layouts
class Grid:
    def __init__(self, card_wh : Point = (0,0), space_wh : Point = (0,0), start : Point = (0,0)):
        self.card_w, self.card_h = card_wh
        self.space_w, self.space_h = space_wh
        self.start_x, self.start_y = start
    
    def __getitem__(self, item : Point) -> Rect:
        return Rect_Layout( (self.card_w+self.space_w)*item[0] + self.start_x, (self.card_h+self.space_h)*item[1] + self.start_y, self.card_w, self.card_h )