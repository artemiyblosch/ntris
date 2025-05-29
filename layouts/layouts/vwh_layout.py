from layouts.layouts.abs_layout import *
from layouts.observers.Observer import Observer
from typing import Self

vw_lay_observer = Observer(["width","height"]).subscribe(meta_observer)

class ViewScreen_Layout(Layout):
    def __init__(self, width_part : float = 0, height_part : float = 0, offset : int = 0):
        self.vwp = width_part
        self.vhp = height_part
        self.offset = offset
        self.value = 0
        self.subscribe()
    
    def update(self,**kwargs):
        self.value = self.vwp * kwargs["width"] + self.vhp * kwargs["height"] + self.offset
    
    @property
    def observer(self):
        return vw_lay_observer
    
    def __add__(self, other : Self | int) -> Self:
        if isinstance(other,int):
            return ViewScreen_Layout(self.vwp, self.vhp, self.offset + other)
        return ViewScreen_Layout(self.vwp + other.vwp, self.vhp + self.vhp, self.offset + other.offset)