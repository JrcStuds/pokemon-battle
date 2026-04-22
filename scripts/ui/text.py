import pygame
import assets.config.settings as settings



class Text():
    def __init__(self, pos: tuple, text: str):
        self.font = pygame.font.SysFont("arial", 12)
        self.pos = pos
        self.text = text


    def draw(self) -> list:
        blits = []
        t = self.font.render(self.text, True, "#000000")
        blits.append((t, self.pos))
        return blits