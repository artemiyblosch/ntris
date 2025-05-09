class Mode:
    def __init__(self, mode : str, init : bool = True):
        self.mode = mode
        self.init = init
        self.gen_range = (1,1)
    
    def set_mode(self, mode : str, init : bool = True):
        self.mode = mode
        self.init = init
        return self

    def set_gen(self, gen_range : tuple[int,int]):
        if gen_range[1] < gen_range[0]: gen_range[0],gen_range[1] = gen_range[1],gen_range[0]
        self.gen_range = gen_range
        return self