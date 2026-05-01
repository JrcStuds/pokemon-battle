import pygame, json
import assets.config.globals as g



class Text():
    def __init__(self, pos: tuple, text: str):
        self.pos = pos
        self.surface = None
        self.update_text(text)


    def draw(self) -> list:
        blit = [(self.surface, self.pos)]
        return blit
    

    def render_text(self, text: str) -> pygame.Surface:
        if not text:
            return pygame.Surface((0, 0))

        with open("assets/data/text_spritesheet.json", "r") as file:
            db = json.load(file)
        text_rects = [db[char] for char in text]
        surface_width = 0
        for char in text_rects: surface_width += char[2]
        surface = pygame.Surface((surface_width, 14))

        pointer = 0
        for char in text_rects:
            char_surface = g.text_spritesheet.subsurface(char)
            surface.blit(char_surface, (pointer, 0))
            pointer += char[2]
        surface.set_colorkey((255, 255, 255))

        return surface
    

    def update_text(self, text: str):
        self.surface = self.render_text(text)