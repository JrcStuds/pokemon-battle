import pygame
import assets.config.settings as s



class SceneBaseClass():
    def __init__(self, rect: pygame.Rect = s.DISPLAY_RECT):
        self.rect = rect

        self.background: str = None
        self.elements: list = []


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for element in self.elements:
                if hasattr(element, "is_clicked"):
                    element.is_clicked(pygame.mouse.get_pos())

                    
    def update(self, dt): pass


    def draw(self) -> list:
        surface = pygame.Surface(self.rect.size)
        if self.background: surface.fill(self.background)

        fblits = []
        for element in self.elements:
            if hasattr(element, "draw"):
                fblits.extend(element.draw())
        surface.fblits(fblits)

        return [(surface, self.rect.topleft)]
    

    def add_elements(self, *elements):
        for element in elements:
            self.elements.append(element)