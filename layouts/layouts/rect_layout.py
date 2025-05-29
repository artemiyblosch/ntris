class Rect_Layout:
    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
    
    def __setattr__(self,name,value):
        if isinstance(value,int):
            object.__setattr__(self, name, wrap(value))
            return self
        object.__setattr__(self, name, value)

    @property
    def rect_tuple(self):
        return (self.left, self.top, self.width, self.height)

    def __repr__(self):
        return f"RL<Computed: {self.rect_tuple}, (\n\t{self.get("left")},\n\t{self.get("top")},\n\t{self.get("width")},\n\t{self.get("height")}\n)>"
    
    def __getattribute__(self, name):
        if name in ["left","top","width","height"]:
            return object.__getattribute__(self,name).value
        return object.__getattribute__(self,name)
    
    def get(self, name):
        return object.__getattribute__(self,name)
    
    def __iter__(self):
        return iter([self.get("left"),self.get("top"),self.get("width"),self.get("height")])

class wrap:
    def __init__(self,value):
        self.value = value
    
    def __repr__(self):
        return f"{self.value}w"