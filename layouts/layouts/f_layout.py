from layouts.layouts.abs_layout import Layout
from layouts.observers.Observer import Observer

f_lay_observer = Observer()

class Functional_Layout(Layout):
    def __init__(self, func):
        self.func = func
        self.value = 0
    
    def update(self,**kwargs):
        self.value = self.func(kwargs)
    
    @property
    def observer(self):
        return f_lay_observer