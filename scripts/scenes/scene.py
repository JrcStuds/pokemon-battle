import pygame
import assets.config.globals as g



class SceneBaseClass():
    def __init__(self, rect: pygame.Rect = g.DISPLAY_RECT, background: str = None):
        self.rect = rect

        self.background: str = background
        self.elements: list = []   # list of ui elements or other scenes


    def handle_event(self, event):
        for element in self.elements:
            if hasattr(element, "handle_event"):
                element.handle_event(event)

                    
    def update(self, dt):
        pass


    def draw(self) -> list:
        blits = []

        # create surface based on scene size as background
        if self.background:
            bg_surf = pygame.Surface(self.rect.size)
            bg_surf.fill(self.background)
            blits.append((bg_surf, (self.rect.topleft)))

        # pass down draw function to elements and extend the overall blit list
        # earlier elements in self.elements will be blitted first -> at the bottom
        for element in self.elements:
            if hasattr(element, "draw"):
                blits.extend(element.draw())

        return blits
    

    def add_elements(self, *elements):
        for element in elements:
            self.elements.append(element)