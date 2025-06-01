from types_ import Point
import pygame as pg
from assets_lib import draw_on, get_image
from mapgen.tile import Tile
from typing import Self

class Figure:
    def __init__(self, figure : list[Point], color : pg.Color):
        self.figure = figure
        self.color = color
    
    def get_fig_preview(self, size : int = 100) -> pg.Surface:
        fig = self.normalized().figure
        x_min = min(fig, key = lambda a: a[0])[0]
        y_min = min(fig, key = lambda a: a[1])[1]
        x_max = max(fig, key = lambda a: a[0])[0]
        y_max = max(fig, key = lambda a: a[1])[1]

        factor = size/(max(x_max - x_min, y_max - y_min)+1)
        factor = min(16,factor)

        w = factor*(x_max-x_min+1)
        h = factor*(y_max-y_min+1)

        fig_surf = pg.Surface((size,size))
        tile = get_image("tile_block.jpg")
        tile = pg.transform.scale_by(tile,factor/16)

        for t in fig:
            draw_on( fig_surf, tile, (t[0]*factor + (size-w)/2, t[1]*factor + (size-h)/2), self.color )
        return fig_surf
    
    def apply_to(self, map, tag : str = "a"):
        for i in self.figure:
            map[i] = Tile(tag, self.color)
        return map
    
    def normalized(self) -> Self:
        fig = Figure(self.figure,self.color)
        x_min = min(fig.figure, key = lambda a: a[0])[0]
        y_min = min(fig.figure, key = lambda a: a[1])[1]
        fig.figure = [(point[0]-x_min, point[1]-y_min) for point in fig.figure]
        return fig
    
    def apply_pos(self, pos : Point):
        self.figure = [(point[0]+pos[0], point[1]+pos[1]) for point in self.normalized().figure]