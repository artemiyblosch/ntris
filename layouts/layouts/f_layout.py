from layouts.layouts.abs_layout import *
from layouts.observers.Observer import Observer

f_lay_observer = Observer().subscribe(meta_observer)

class Functional_Layout(Layout):
    def __init__(self, func):
        self.func = func
        self.value = 0
        self.subscribe()
    
    def update(self,**kwargs):
        self.value = self.func(kwargs)
    
    @property
    def observer(self):
        return f_lay_observer