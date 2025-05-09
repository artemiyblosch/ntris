import utils as u
import pygame as pg
from types_ import Point

class Tile:
    def __init__(self, figure : str | None = None, color : pg.Color = (127,127,127)):
        self.figure = figure
        self.color = color

class Map:
    def __init__(self):
        self.map = {}
    
    def __getitem__(self, key : Point) -> None | Tile:
        if key[0] not in self.map: return None
        if key[1] not in self.map[key[0]]: return None
        return self.map[key[0]][key[1]]
    
    def __setitem__(self, key : Point, value : None | Tile):
        if key[0] not in self.map: self.map[key[0]] = {}
        self.map[key[0]][key[1]] = value
    
    def __str__(self):
        return "\n".join(["".join(["#" if self[i,j] != None else " " for j in range(10)]) for i in range(20)])

    def __repr__(self):
        return self.map

    def __delitem__(self, key : Point):
        if key[0] not in self.map: return
        if key[1] not in self.map[key[0]]: return
        del self.map[key[0]][key[1]]

    def seek_figure(self, figure : str = "a"):
        raw_map = [[(i,j) for j in self.map[i] if self[i,j] != None and self[i,j].figure == figure] for i in self.map]
        return [x for xs in raw_map for x in xs]
    
    def __contains__(self, item : Point):
        return item[0] in self.map and item[1] in self.map[item[0]]

    def move(self, figure : str = "a", direction : Point = (0,-1)):
        f_coords = self.seek_figure(figure)
        color = self[f_coords[0]].color
        for i in f_coords:
            del self[i]
        for i in f_coords:
            self[i[0] + direction[0], i[1] + direction[1]] = Tile(figure, color)
    
    def can_move(self, figure : str = "a", direction : Point = (0,-1), width = 21):
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
        center = (round(u.avg([i[0] for i in f_coords])), round(u.avg([i[1] for i in f_coords])))
        for i in f_coords:
            del self[i]
        for i in f_coords:
            self[u.rotate(i,center)] = Tile(figure, color)
    
    def are_valid_coords(self, f_coords : list[Point], figure : str = "a", width : int = 21):
        for i in f_coords:
            if i[1] < 0: return False
            if not (0 <= i[0] < width): return False
            if i in self and\
               (self[i] or Tile(None)).figure != figure:
                return False
        return True
    
    def rotate(self, figure : str = "a"):
        f_coords = self.seek_figure(figure)
        color = self[f_coords[0]].color
        center = (round(u.avg([i[0] for i in f_coords])), round(u.avg([i[1] for i in f_coords])))
        for i in f_coords:
            del self[i]
        for i in f_coords:
            self[u.rotate(i,center)] = Tile(figure, color)
    
    def can_rotate(self, figure : str = "a", width : int = 21):
        f_coords = self.seek_figure(figure)
        center = (round(u.avg([i[0] for i in f_coords])), round(u.avg([i[1] for i in f_coords])))
        f_coords = [u.rotate(i,center) for i in f_coords]
        return self.are_valid_coords(f_coords, figure, width)
    
    def flip(self, figure : str = "a"):
        f_coords = self.seek_figure(figure)
        color = self[f_coords[0]].color
        center = round(u.avg([i[0] for i in f_coords]))
        for i in f_coords:
            del self[i]
        for i in f_coords:
            self[u.flip(i,center)] = Tile(figure, color)
    
    def can_flip(self, figure : str = "a", width : int = 21):
        f_coords = self.seek_figure(figure)
        center = round(u.avg([i[0] for i in f_coords]))
        f_coords = [u.flip(i,center) for i in f_coords]
        return self.are_valid_coords(f_coords, figure, width)
    
    def get_line(self, line : int, width : int = 21):
        return [self[i,line] for i in range(width)]
    
    def delete_line(self, line : int, width : int = 21):
        for i in range(width): del self[i,line]

        coords = []
        for x in self.map:
            for y in self.map[x]:
                if y > line:
                    coords.append((x,y))
        coords.sort(key=lambda a: a[1])
        for i in coords:
            self[i[0],i[1]-1] = self[i]
            del self[i]