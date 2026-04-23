import pygame
import assets.config.globals as g



class Text():
    def __init__(self, pos: tuple, text: str, col: str = "#000000"):
        self.font = pygame.font.SysFont("arial", 12)
        self.pos = pos
        self.text = text
        self.surface = self.font.render(self.text, False, col)


    def draw(self) -> list:
        blit = [(self.surface, self.pos)]
        return blit