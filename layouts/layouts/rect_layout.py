import pygame as pg

class Rect_Layout:
    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
    
    def __setattr__(self,name,value):
        if isinstance(value,int):
            object.__setattr__(self, name, int_wrap(value))
            return self
        object.__setattr__(self, name, value)

    @property
    def rect_tuple(self):
        return (self.left, self.top, self.width, self.height)
    
    def __getattribute__(self, name):
        if name in ["left","right","width","height"]:
            return object.__getattribute__(self,name).value

class int_wrap:
    def __init__(self,value):
        self.value = value

print(Rect_Layout(5,5,10,5))