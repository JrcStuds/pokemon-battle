import pygame
import assets.config.globals as g



class Cursor():
    def __init__(self, buttons: list, type: str, visible: bool = True):
        self.surface = pygame.Surface((2, 2))
        self.surface.fill("red")
        self.visible = visible

        self.cursor_elements = {}   # assign value to each button provided
        for i, button in enumerate(buttons):
            self.cursor_elements[i] = button
        self.idx = 0
        self.pos = self.cursor_elements[self.idx].rect.center

        self.handle_event = None   # cursor HAS a movement behaviour (composition)
        match type:
            case "four_button": self.handle_event = self.four_button_handle_event

    
    def draw(self) -> list:
        return [(self.surface, self.pos)]
    

    def four_button_handle_event(self, event):
        if g.keys["up"] and self.idx >= 2:   # if the cursor is in the bottom 2
            self.idx -= 2
            self.pos = self.cursor_elements[self.idx].rect.center
        if g.keys["down"] and self.idx <= 1:   # if the cursor is in the top 2
            self.idx += 2
            self.pos = self.cursor_elements[self.idx].rect.center
        if g.keys["left"] and self.idx % 2 == 1:   # if the cursor is on the right
            self.idx -= 1
            self.pos = self.cursor_elements[self.idx].rect.center
        if g.keys["right"] and self.idx % 2 == 0:   # if the cursor is on the left
            self.idx += 1
            self.pos = self.cursor_elements[self.idx].rect.center
        if g.keys["a"] and hasattr(self.cursor_elements[self.idx], "click"):   # click button under cursor
                self.cursor_elements[self.idx].click()