from layouts.layouts.abs_layout import *
from layouts.observers.Observer import Observer
from typing import Self

vw_lay_observer = Observer(["width","height"]).subscribe(meta_observer)

class ViewScreen_Layout(Layout):
    def __init__(self, width_part : float = 0, height_part : float = 0, offset : int = 0):
        self.vwp = width_part
        self.vhp = height_part
        self.offset = offset
        self.value = 10
        self.subscribe()
        self.debug = False

    def debug(self):
        self.debug = True
    
    def update(self,**kwargs):
        self.value = self.vwp * kwargs["width"] + self.vhp * kwargs["height"] + self.offset
    
    def __repr__(self):
        return f"VWL<Computed:{self.value}, {self.vwp}vw+{self.vhp}vh+{self.offset}>"
    
    @property
    def observer(self):
        return vw_lay_observer
    
    def __add__(self, other : Self | int) -> Self:
        if isinstance(other, int | float):
            return ViewScreen_Layout(self.vwp, self.vhp, self.offset + other)
        return ViewScreen_Layout(self.vwp + other.vwp, self.vhp + other.vhp, self.offset + other.offset)
    
    def __radd__(self, other : Self | int) -> Self:
        return self + other
    
    def __sub__(self, other : Self | int) -> Self:
        if isinstance(other, int | float):
            return ViewScreen_Layout(self.vwp, self.vhp, self.offset - other)
        return ViewScreen_Layout(self.vwp - other.vwp, self.vhp - other.vhp, self.offset - other.offset)

    def __mul__(self, other : Self | int) -> Self:
        if isinstance(other,int):
            return ViewScreen_Layout(self.vwp * other, self.vhp * other, self.offset * other)
        return NotImplemented#return ViewScreen_Layout(self.vwp * other.vwp, self.vhp * self.vhp, self.offset * other.offset)