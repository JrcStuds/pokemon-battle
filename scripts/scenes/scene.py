import pygame
import assets.config.globals as g



class SceneBaseClass():
    def __init__(self, background = None, rect: pygame.Rect = g.DISPLAY_RECT):
        self.rect = rect

        self.background = background
        self.elements: list = []   # list of ui elements or other scenes

        self.bg_surf = None
        if type(background) == str:
            self.bg_surf = pygame.Surface(self.rect.size)
            self.bg_surf.fill(background)
        if type(background) == pygame.Surface:
                self.bg_surf = background


    def handle_event(self, event):
        for element in self.elements:
            if hasattr(element, "handle_event"):
                element.handle_event(event)

                    
    def update(self, dt):
        pass


    def draw(self) -> list:
        blits = []
        if self.bg_surf:
            blits.append((self.bg_surf, self.rect.topleft))

        # pass down draw function to elements and extend the overall blit list
        # earlier elements in self.elements will be blitted first -> at the bottom
        for element in self.elements:
            if hasattr(element, "draw"):
                blits.extend(element.draw())

        return blits
    

    def add_elements(self, *elements):
        for element in elements:
            self.elements.append(element)