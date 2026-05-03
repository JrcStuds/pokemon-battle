import pygame



class ImageButton():
    def __init__(self, callback, pos: tuple, image_unselected: pygame.Surface, image_selected: pygame.Surface, selected: bool = False):
        self.callback = callback
        self.pos = pos
        self.selected = selected
        self.image_unselected = image_unselected
        self.image_selected = image_selected
        self.surface = self.image_selected if self.selected else self.image_unselected


    def draw(self) -> list:
        blits = [(self.surface, self.pos)]
        return blits


    def click(self):
        if self.callback:
            self.callback()


    def change_select(self):
        self.selected = not self.selected
        self.surface = self.image_selected if self.selected else self.image_unselected