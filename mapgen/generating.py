from mapgen.map import *
from random import randint, choice


def gen_figure(at : tuple[int,int] = (10,42), size_range : int = (3,13), width : int = 21, figure : str = "a"):
    if randint(1,50) == 1: return [at]
    if randint(1,30) == 1: return [at,(at[0],at[1]+1)]
    if randint(1,1000) == 1: return [(i,at[1]) for i in range(width)]
    return gen_raw_figure(at,randint(*size_range),width)

def apply_to(map : Map, figure, tag : str = "a"):
    color = (randint(40,160),randint(40,160),randint(40,160))
    for i in figure:
        map[i] = Tile(tag,color)
    return map

def gen_raw_figure(at : tuple[int,int] = (10,42), size : int = 4, width : int = 21):
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
    
    return coords