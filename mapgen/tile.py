import pygame as pg

class Tile:
    def __init__(self, figure : str | None = None, color : pg.Color = (127,127,127)):
        self.figure = figure
        self.color = color