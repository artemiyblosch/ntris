from mapgen import *
from random import randint, choice


def gen_figure(map, at : tuple[int,int] = (10,42), size_range : int = (3,13), width : int = 21, figure : str = "a"):
    color = (randint(20,150),randint(20,150),randint(20,150))
    if randint(1,50) == 1:
        map[at] = Tile(figure,color)
        return
    if randint(1,30) == 1:
        map[at] = Tile(figure,color)
        map[at[0],at[1]+1] = Tile(figure,color)
        return
    if randint(1,1000) == 1:
        for i in range(width):
             map[i,at[1]] = Tile(figure,color)
        return
    return gen_raw_figure(map,at,randint(*size_range),width,figure)

def gen_raw_figure(map, at : tuple[int,int] = (10,42), size : int = 4, width : int = 21, figure : str = "a"):
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
        
        if randint(1,10) == 1:
            coords = [(at[0],at[1]+i) for i in range(size)]
        
        for i in coords:
            map[i] = Tile(figure,color)