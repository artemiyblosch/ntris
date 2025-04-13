from random import choice

class Tile:
    def __init__(self, figure : str | None = None, color : str = "#aaaaaa"):
        self.figure = figure
        self.color = color

class Map:
    def __init__(self):
        self.map = {}
    
    def __getitem__(self, key : tuple[int,int]) -> None | Tile:
        if key[1] == ...:
            return self.map.setdefault(key[0],{})
        return self.map.setdefault(key[0],{}).setdefault(key[1])
    
    def __setitem__(self, key : tuple[int,int], value : None | Tile):
        if key[0] not in self.map: self.map[key[0]] = {}
        self.map[key[0]][key[1]] = value
    
    def __str__(self):
        return "\n".join(["".join(["#" if self[i,j] != None else " " for j in range(20)]) for i in range(10)])

    def seek_figure(self, figure : str = "a"):
        raw_map = [[(i,j) for j in self[i,...] if self[i,j].figure == figure] for i in self.map]
        return [x for xs in raw_map for x in xs]

    def gen_figure(self, at : tuple[int,int] = (20,5), size : int = 4, width : int = 11, figure : str = "a"):
        for _ in range(1,size):
            coords = [at]
            new_coords = []
            for i in coords:
                new_coords.append((i[0],i[1] + 1))
                new_coords.append((i[0],i[1] - 1))
                new_coords.append((i[0] + 1,i[1]))
                new_coords.append((i[0] - 1,i[1]))
            new_coords = [i for i in new_coords if 0 < i[0] < width + 1 and i not in coords]
            coords.append(choice(new_coords))
        
        for i in coords:
            self[i] = Tile(figure)
        