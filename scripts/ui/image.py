import pygame
import assets.config.globals as g



class Image():
    def __init__(self, pos: tuple, type: str, name: str):
        self.pos = pos
        self.type = type
        self.name = name
        self.surface = self.init_surface_from_spritesheet()


    def draw(self) -> list:
        blit = [(self.surface, self.pos)]
        return blit

    
    def init_surface_from_spritesheet(self):
        size = 0
        sprite = g.SPRITESHEET[self.type][self.name]
        match self.type:
            case "mini": size = 32
        
        surface = g.pokemon_spritesheet.subsurface(pygame.Rect(sprite[0], sprite[1], size, size))
        surface.set_colorkey(sprite[1])

        return surface