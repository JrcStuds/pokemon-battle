import pygame
import assets.config.settings as settings



class SceneBaseClass():
    def __init__(self):
        self.background: str = ""
        self.elements: list = []


    def draw(self) -> pygame.Surface:
        surface = pygame.Surface(settings.DISPLAY_SIZE)
        surface.fill(self.background)

        fblits = []
        for element in self.elements:
            if hasattr(element, "draw"):
                fblits.extend(element.draw())
        surface.fblits(fblits)

        return surface