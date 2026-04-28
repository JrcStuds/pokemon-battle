import pygame
import assets.config.globals as g
import scripts.ui as ui
from .menu_base_scene import BattleMenuSceneBaseClass



class FourButtonMenuBaseClass(BattleMenuSceneBaseClass):
    def __init__(self, battle):
        super().__init__(battle)

        self.rect = g.FOUR_BUTTON_RECTS["container"]
        self.background = "dodgerblue"


    def init_cursor(self):
        self.cursor_elements = {
            0: self.elements[0],
            1: self.elements[1],
            2: self.elements[2],
            3: self.elements[3],
        }
        self.cursor_idx = 0
        self.cursor = ui.Cursor(pos=self.cursor_elements[self.cursor_idx].rect.center, visible=True)
        self.add_elements(self.cursor)
    
    
    def handle_event(self, event):
        if g.keys["up"] and self.cursor_idx >= 2:
            self.cursor_idx -= 2
            self.cursor.pos = self.cursor_elements[self.cursor_idx].rect.center
        if g.keys["down"] and self.cursor_idx <= 1:
            self.cursor_idx += 2
            self.cursor.pos = self.cursor_elements[self.cursor_idx].rect.center
        if g.keys["left"] and self.cursor_idx % 2 == 1:
            self.cursor_idx -= 1
            self.cursor.pos = self.cursor_elements[self.cursor_idx].rect.center
        if g.keys["right"] and self.cursor_idx % 2 == 0:
            self.cursor_idx += 1
            self.cursor.pos = self.cursor_elements[self.cursor_idx].rect.center
        if g.keys["a"] and hasattr(self.cursor_elements[self.cursor_idx], "click"):
                self.cursor_elements[self.cursor_idx].click()
        
        for element in self.elements:
            if hasattr(element, "handle_event"):
                element.handle_event(event)