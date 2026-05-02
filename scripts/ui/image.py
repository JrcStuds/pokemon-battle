import pygame, json
import assets.config.globals as g



class Image():
    def __init__(self, pos: tuple, spritesheet: str, name: str, type: str = None):
        self.pos = pos
        self.type = type
        self.name = name.lower()
        self.surface = self.init_surface_from_spritesheet(spritesheet)


    def draw(self) -> list:
        blit = [(self.surface, self.pos)]
        return blit

    
    def init_surface_from_spritesheet(self, spritesheet):
        with open(f"assets/data/{spritesheet}_spritesheet.json", "r") as file:
            spritesheet_db = json.load(file)
        sprite = spritesheet_db[self.type][self.name] if self.type else spritesheet_db[self.name]
        surface = g.spritesheets[spritesheet].subsurface(sprite)
        return surface