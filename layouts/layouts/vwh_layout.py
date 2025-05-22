from layouts.layouts.abs_layout import Layout
from layouts.observers.Observer import Observer

vw_lay_observer = Observer()

class ViewScreen_Layout(Layout):
    def __init__(self, width_part : float, height_part : float):
        self.vwp = width_part
        self.vhp = height_part
        self.value = 0
    
    def update(self,**kwargs):
        self.value = self.vwp * kwargs["width"] + self.vhp * kwargs["height"]
    
    @property
    def observer(self):
        return vw_lay_observer