from layouts.layouts.abs_layout import Layout
from layouts.layouts.rect_layout import Rect_Layout
import pygame as pg

def supports_layouts(cls : type):
    '''Unwraps the values of the layouts in the props'''
    def get_layout(self, item):
        attr = object.__getattribute__(self, item)

        if isinstance(attr, Layout): return attr.value
        if isinstance(attr, Rect_Layout):
            return pg.Rect(attr.rect_tuple)
        
        return attr
    
    def pure_get(self, item):
        return object.__getattribute__(self, item)
    
    cls.__getattribute__ = get_layout
    cls.get_layout = pure_get
    return cls