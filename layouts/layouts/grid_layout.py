from types_ import Point
from pygame import Rect
from layouts.decor.layouty import supports_layouts

@supports_layouts
class Grid:
    def __init__(self, card_wh : Point, space_wh : Point):
        self.card_w, self.card_h = card_wh
        self.space_w, self.space_h = space_wh
    
    def __getitem__(self, item : Point) -> Rect:
        return Rect( (self.card_w+self.space_w)*item, (self.card_h+self.space_h)*item, self.card_w, self.card_h )
    
    @property
    def card_wh(self):
        return (self.card_w, self.card_h)
    
    @property
    def space_wh(self):
        return (self.space_w, self.space_h)