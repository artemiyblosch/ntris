import pygame as pg
from types_ import Point

def get_image(path : str, alpha : bool = False) -> pg.Surface:
    if alpha:
        return pg.image.load(f'./assets/images/{path}').convert_alpha()
    return pg.image.load(f'./assets/images/{path}').convert()

def draw_on(screen : pg.Surface, image : str | pg.Surface, at : Point, tint : pg.Color | None = None):
    if isinstance(image,str): img = get_image(image)
    else: img = image
    
    if tint != None:
        img.fill(tint, special_flags=pg.BLEND_MULT)
    screen.blit(img,at)