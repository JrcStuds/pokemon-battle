import pygame, json
import assets.config.globals as g



class Text():
    def __init__(self, pos: tuple, text: str, type: str = "regular", col: str = "dark"):
        self.pos = pos
        self.surface = None
        self.type = type   # regular or small
        self.col = col   # dark, light, dark_alt, or light_alt
        self.update_text(text)


    def draw(self) -> list:
        blit = [(self.surface, self.pos)]
        return blit
    

    def render_text(self, text: str) -> pygame.Surface:
        if not text:
            return pygame.Surface((0, 0))

        with open("assets/data/spritesheets/text.json", "r") as file:
            db = json.load(file)
        text_rects = [db[self.type][char] for char in text]
        surface_width = 0
        for char in text_rects: surface_width += char[2]
        surface = pygame.Surface((surface_width, 14), pygame.SRCALPHA)

        pointer = 0
        for char in text_rects:
            char_surface = g.spritesheets["text"].subsurface(char)
            surface.blit(char_surface, (pointer, 0))
            pointer += char[2]

        self.palette_swap(surface=surface, end_palette=self.col)

        return surface
    

    def update_text(self, text: str):
        self.surface = self.render_text(text)


    def palette_swap(self, surface: pygame.Surface, end_palette: str, start_palette: str = "dark"):
        with pygame.PixelArray(surface) as pixels:
            pixels.replace(g.TEXT_COLOUR_PALETTES[start_palette][0], g.TEXT_COLOUR_PALETTES[end_palette][0])
            pixels.replace(g.TEXT_COLOUR_PALETTES[start_palette][1], g.TEXT_COLOUR_PALETTES[end_palette][1])
        return