import pygame
import assets.config.globals as g



class Text():
    def __init__(self, pos: tuple, text: str, col: str = "#000000"):
        self.font = pygame.font.SysFont("arial", 8)
        self.pos = pos
        self.col = col
        self.surface = None
        self.update_text(text=text)


    def draw(self) -> list:
        blit = [(self.surface, self.pos)]
        return blit
    

    def update_text(self, text: str):
        self.surface = self.font.render(text, False, self.col)