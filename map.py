from random import choice, randint

class Tile:
    def __init__(self, figure : str | None = None, color : tuple[int,int,int] = (127,127,127)):
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
        return "\n".join(["".join(["#" if self[i,j] != None else " " for j in range(10)]) for i in range(20)])

    def __repr__(self):
        return self.map

    def __delitem__(self, name : tuple[int,int]):
        del self.map[name[0]][name[1]]

    def seek_figure(self, figure : str = "a"):
        raw_map = [[(i,j) for j in self.map[i] if self[i,j] != None and self[i,j].figure == figure] for i in self.map]
        return [x for xs in raw_map for x in xs]

    def gen_figure(self, at : tuple[int,int] = (10,42), size : int = 4, width : int = 21, figure : str = "a"):
        color = (randint(20,150),randint(20,150),randint(20,150))
        coords = [at]
        for _ in range(1,size):
            new_coords = []
            for i in coords:
                new_coords.append((i[0],i[1] + 1))
                new_coords.append((i[0],i[1] - 1))
                new_coords.append((i[0] + 1,i[1]))
                new_coords.append((i[0] - 1,i[1]))
            new_coords = [i for i in new_coords if 0 < i[0] < width + 1 and i not in coords]
            coords.append(choice(new_coords))
        
        for i in coords:
            self[i] = Tile(figure,color)
    
    def __contains__(self, item : tuple[int,int]):
        return item[0] in self.map and item[1] in self.map[item[0]]

    def move(self, figure : str = "a", direction : tuple[int,int] = (0,-1)):
        f_coords = self.seek_figure(figure)
        color = self[f_coords[0]].color
        for i in f_coords:
            del self[i]
        for i in f_coords:
            self[i[0] + direction[0], i[1] + direction[1]] = Tile(figure, color)
    
    def can_move(self, figure : str = "a", direction : tuple[int,int] = (0,-1), width = 21):
        f_coords = self.seek_figure(figure)
        f_coords = [(i[0] + direction[0], i[1] + direction[1]) for i in f_coords]
        return self.are_valid_coords(f_coords)
    
    def remove_figure_status(self, figure : str = "a"):
        for i in self.map:
            for j in self.map[i]:
                self[i,j] = Tile(None if self[i,j].figure == figure else self[i,j].figure,self[i,j].color)

    def rotate(self, figure : str = "a"):
        f_coords = self.seek_figure(figure)
        color = self[f_coords[0]].color
        center = (round(avg([i[0] for i in f_coords])), round(avg([i[1] for i in f_coords])))
        for i in f_coords:
            del self[i]
        for i in f_coords:
            self[rotate(i,center)] = Tile(figure, color)
    
    def can_rotate(self, figure : str = "a", width : int = 21):
        f_coords = self.seek_figure(figure)
        center = (round(avg([i[0] for i in f_coords])), round(avg([i[1] for i in f_coords])))
        f_coords = [rotate(i,center) for i in f_coords]
        return self.are_valid_coords(f_coords, figure, width)
    
    def are_valid_coords(self, f_coords, figure : str = "a", width : int = 21):
        for i in f_coords:
            if i[1] < 0: return False
            if not (0 < i[0] < width): return False
            if i in self and\
               (self[i] or Tile(None)).figure != figure:
                return False
        return True

def avg(lst : list):
    return sum(lst)/len(lst)

def enum(map):
    ret = []
    for x in map.map:
        for y in map.map[x]:
            ret.append([(x,y),map[x,y]])
    return ret

def rotate(p : tuple[int,int], a : tuple[int,int],):
  return [-p[1]+a[1]+a[0],p[0]-a[0]+a[1]]