from typing import Self
class Observer:
    def __init__(self, depends : list | None = None):
        self.depends = depends
        self.observants = []
        self.children : list[Self] = None
        self.old_args = {}
    
    def subscribe(self, other : Self):
        if other.children == None:
            other.children = [self]
        else:
            other.children.append(self)
    
    def add(self, other):
        self.observants.append(other)
    
    def remove(self, other):
        self.observants.remove(other)

    def observe(self,**kwargs):
        for i in self.observants:
            i.update(**kwargs)
        
        if self.old_args != kwargs:
            for i in self.children:
                if i.depends == None:
                    i.observe(kwargs)
                    continue
                if i.is_depend_triggered(self.old_args, kwargs): i.observe(kwargs)
    
    def is_depend_triggered(self, old : dict, new : dict) -> bool:
        for i in self.depends:
            if old[i] != new[i]: return True
        return False