import pygame
import assets.config.globals as g



class Cursor():
    def __init__(self, pos: tuple = (0, 0), visible: bool = False):
        self.surface = pygame.Surface((2, 2))
        self.surface.fill("red")
        self.pos = pos
        self.visible = visible

    
    def draw(self) -> list:
        return [(self.surface, self.pos)]