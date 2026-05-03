import pygame, json
import assets.config.globals as g



def create_surface_from_spritesheet(spritesheet, name, type = None) -> pygame.Surface:
    with open(f"assets/data/spritesheets/{spritesheet}.json", "r") as file:
        spritesheet_db = json.load(file)
    sprite = spritesheet_db[type][name] if type else spritesheet_db[name]
    surface = g.spritesheets[spritesheet].subsurface(sprite)
    return surface



class Image():
    def __init__(self, pos: tuple, spritesheet: str, name: str, type: str = None):
        self.pos = pos
        self.type = type
        self.name = name.lower()
        self.surface = create_surface_from_spritesheet(spritesheet, self.name, self.type)


    def draw(self) -> list:
        blit = [(self.surface, self.pos)]
        return blit