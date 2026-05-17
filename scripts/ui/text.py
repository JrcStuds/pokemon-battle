import pygame, json
import assets.config.globals as g



class Text():
    def __init__(self, pos: tuple, text: str, type: str = "regular", col: str = "dark", alignment: str = "left"):
        self.pos = pos
        self.surface = None
        self.type = type   # regular or small
        self.col = col   # dark, light, dark_alt, or light_alt
        self.alignment = alignment
        self.offset = 0
        self.update_text(text)

    def draw(self) -> list:
        blit = [(self.surface, (self.pos[0]+self.offset, self.pos[1]))]
        return blit
    

    # creates a surface based on the provided string using self.type and self.col
    def render_text(self, text: str) -> pygame.Surface:
        if not text:
            return pygame.Surface((0, 0))

        with open("assets/data/spritesheets/text.json", "r") as file:
            db = json.load(file)
        text_rects = []
        special_char = False
        for char in text:
            if char == "$":
                special_char = True
                continue
            if special_char:
                text_rects.append(db[self.type]["$"][char])
                special_char = False
                continue
            text_rects.append(db[self.type][char])
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
    

    # re-renders text and replaces surface
    def update_text(self, text: str):
        self.surface = self.render_text(text)
        match self.alignment:
            case "left": self.offset = 0
            case "right": self.offset = -(self.surface.get_width())
            case "center": self.offset = -(self.surface.get_width() / 2)


    # converts all colours in the surface to others defined in g.TEXT_COLOUR_PALETTES
    def palette_swap(self, surface: pygame.Surface, end_palette: str, start_palette: str = "dark"):
        with pygame.PixelArray(surface) as pixels:
            pixels.replace(g.TEXT_COLOUR_PALETTES[start_palette][0], g.TEXT_COLOUR_PALETTES[end_palette][0])
            pixels.replace(g.TEXT_COLOUR_PALETTES[start_palette][1], g.TEXT_COLOUR_PALETTES[end_palette][1])
        return