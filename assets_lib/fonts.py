import pygame as pg

fonts = {}
def load_font(name : str, args):
    fonts[name] = pg.font.Font(*args)

def get_font(name : str):
    if name not in fonts: return pg.font.Font('./assets/fonts/JOYSTIX.otf',34)
    return fonts[name]

texts = {}
def precompile_text(text : str, font_name : str, color : pg.color.Color = (255,255,255)):
    if (text, font_name, color) not in texts: texts[(text, font_name,color)] = get_font(font_name).render(text, False, color)
    return texts[(text, font_name, color)]
