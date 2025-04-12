class Tile:
    def __init__(self, figure : str, color : str):
        self.figure = figure
        self.color = color

class Map:
    def __init__(self):
        self.map = {}
    
    def __getitem__(self, key : tuple[int,int]) -> None | Tile:
        return self.map.setdefault(key[0],{}).setdefault(key[1])
    
    def __setitem__(self, key : tuple[int,int], value : None | Tile):
        if key[0] not in self.map: self.map[key[0]] = {}
        self.map[key[0]][key[1]] = value
    def __str__(self):
        return "\n".join(["".join(["#" if self[i,j] != None else " " for j in range(20)]) for i in range(10)])
