import pygame
import assets.config.globals as g
from .text import Text



class Button():
    def __init__(self, callback, rect: pygame.Rect, text: str = None, type: str = "regular"):
        self.callback = callback
        self.rect = rect
        self.text = Text(self.rect.topleft, text, type)


    def draw(self) -> list:
        surface = pygame.Surface(self.rect.size)
        surface.fill("darkseagreen")

        blits = [(surface, self.rect.topleft)]
        blits.extend(self.text.draw())
        return blits

    
    def click(self):
        if self.callback:
            self.callback()
    
