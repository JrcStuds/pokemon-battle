import pygame
import assets.config.settings as s



class Container():
    def __init__(self, elements: list = []):
        self.elements = elements
    

    def draw(self):
        blits = []
        for element in self.elements:
            if hasattr(element, "draw"):
                blits.extend(element.draw())
        return blits
    

    def add_elements(self, *elements):
        for element in elements:
            self.elements.append(element)