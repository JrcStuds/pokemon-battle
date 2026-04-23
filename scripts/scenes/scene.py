import pygame
import assets.config.globals as g



class SceneBaseClass():
    def __init__(self, rect: pygame.Rect = g.DISPLAY_RECT, background: str = None):
        self.rect = rect

        self.background: str = background
        self.elements: list = []


    def handle_event(self, event):
        pass

                    
    def update(self, dt):
        pass


    def draw(self) -> list:
        blits = []

        if self.background:
            bg_surf = pygame.Surface(self.rect.size)
            bg_surf.fill(self.background)
            blits.append((bg_surf, (self.rect.topleft)))

        for element in self.elements:
            if hasattr(element, "draw"):
                blits.extend(element.draw())

        return blits
    

    def add_elements(self, *elements):
        for element in elements:
            self.elements.append(element)