from typing import Self
class Mode:
    def __init__(self : Self, mode : str, init : bool = True):
        self.mode = mode
        self.init = init
        self.gen_range = (1,1)
        self.sandbox_entry = -1
    
    def set_mode(self : Self, mode : str, init : bool = True):
        self.mode = mode
        self.init = init
        return self

    def set_gen(self : Self, gen_range : tuple[int,int]):
        if gen_range[1] < gen_range[0]:
            self.gen_range = (gen_range[1],gen_range[0])
            return self
        self.gen_range = gen_range
        return self
    
    def set_as(self, other : Self):
        self.gen_range = other.gen_range
        self.init = other.init
        self.mode = other.mode
        self.sandbox_entry = other.sandbox_entry
        return self
    
    def debug(self):
        print(f"Mode: {self.mode}, {self.init}, {self.gen_range}")