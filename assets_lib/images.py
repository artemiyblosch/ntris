import pygame as pg
from types_ import Point

def get_image(path : str) -> pg.Surface:
    return pg.image.load(f'./assets/images/{path}').convert()

def draw_on(screen : pg.Surface, path : str, at : Point, tint : pg.Color | None = None):
    img = get_image(path)
    if tint != None:
        img.fill(tint, special_flags=pg.BLEND_MULT)
    screen.blit(img,at)