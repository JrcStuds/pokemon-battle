import pygame
import assets.config.globals as g
from .image import create_surface_from_spritesheet



class HpBar():
    def __init__(self, pos, value: int = 0):
        self.pos = pos
        self.value = value
        self.base = create_surface_from_spritesheet("menus", "hp_bar")
        self.hp = self.create_hp_surface(value)

    
    def draw(self) -> list:
        blits = [
            (self.base, self.pos),
            (self.hp, (self.pos[0]+15, self.pos[1]+2))
        ]
        return blits
    

    def create_hp_surface(self, value) -> pygame.Surface:
        surface = pygame.Surface((48, 3), pygame.SRCALPHA)
        if value <= 6: col = "red"
        elif value <= 24: col = "yellow"
        else: col = "green"
        pygame.draw.rect(surface, g.HP_COLOURS[f"{col}_dark"], (0, 0, value, 1))
        pygame.draw.rect(surface, g.HP_COLOURS[f"{col}_light"], (0, 1, value, 2))
        return surface
    

    def update_value(self, value):
        self.hp = self.create_hp_surface(value)