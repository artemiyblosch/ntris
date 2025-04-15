import pygame as pg

fonts = {}
def load_font(name, args):
    fonts[name] = pg.font.Font(*args)

def get_font(name):
    return fonts[name]

texts = {}
def precompile_text(text, font_name, color = (255,255,255)):
    if (text, font_name) not in texts: texts[(text, font_name)] = get_font(font_name).render(text, False, color)
    return texts[(text, font_name)]
