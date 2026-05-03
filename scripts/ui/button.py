import pygame
import assets.config.globals as g
from .text import Text



class Button():
    def __init__(self, callback, rect: pygame.Rect = pygame.Rect(0, 0, 0, 0), cursor_pos: tuple = None, text: str = None, type: str = "regular", col: str = "dark"):
        self.callback = callback
        self.rect = rect
        self.cursor_pos = cursor_pos if cursor_pos else self.rect.topleft
        self.text = Text(self.rect.topleft, text, type, col) if text else None


    def draw(self) -> list:
        surface = pygame.Surface(self.rect.size)
        surface.fill("darkseagreen")

        blits = [(surface, self.rect.topleft)]
        if self.text:
            blits.extend(self.text.draw())
        return blits

    
    def click(self):
        if self.callback:
            self.callback()
    
