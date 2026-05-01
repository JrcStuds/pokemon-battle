import pygame, json
import assets.config.globals as g



class Image():
    def __init__(self, pos: tuple, type: str, name: str):
        self.pos = pos
        self.type = type
        self.name = name.lower()
        self.surface = self.init_surface_from_spritesheet()


    def draw(self) -> list:
        blit = [(self.surface, self.pos)]
        return blit

    
    def init_surface_from_spritesheet(self):
        with open("assets/data/spritesheet.json", "r") as file:
            spritesheet_db = json.load(file)
        size = spritesheet_db[self.type]["size"]
        sprite = spritesheet_db[self.type][self.name]
        
        surface = g.pokemon_spritesheet.subsurface(pygame.Rect(sprite[0], sprite[1], size, size))
        surface.set_colorkey(sprite[2])

        return surface