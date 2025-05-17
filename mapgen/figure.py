from types_ import Point
import pygame as pg
from assets_lib import draw_on, get_image
from mapgen.map import Map, Tile

class Figure:
    def __init__(self, figure : list[Point], color : pg.Color):
        self.figure = figure
        self.color = color
    
    def get_fig_preview(self) -> pg.Surface:
        fig = self.figure
        x_min = min(fig, key = lambda a: a[0])[0]
        y_min = min(fig, key = lambda a: a[1])[1]
        x_max = max(fig, key = lambda a: a[0])[0]
        y_max = max(fig, key = lambda a: a[1])[1]

        factor = 150/(max(x_max - x_min, y_max - y_min)+1)
        factor = min(16,factor)

        w = factor*(x_max-x_min+1)
        h = factor*(y_max-y_min+1)

        fig_surf = pg.Surface((150,150))
        tile = get_image("tile_block.jpg")
        tile = pg.transform.scale_by(tile,factor/16)

        for t in fig:
            draw_on( fig_surf, tile, ((t[0]-x_min)*factor + (150-w)/2, (t[1]-y_min)*factor + (150-h)/2), self.color )
        return fig_surf
    
    def apply_to(self, map : Map, tag : str = "a"):
        for i in self.figure:
            map[i] = Tile(tag, self.color)
        return map