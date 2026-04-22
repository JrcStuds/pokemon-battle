import pygame
import assets.config.settings as settings



class Button():
    def __init__(self, callback, rect: pygame.Rect, text: str = None):
        self.font = pygame.font.SysFont("arial", 8)
        self.callback = callback
        self.rect = rect
        self.text = text


    def draw(self) -> list:
        blits = []
        b = pygame.Surface(self.rect.size)
        b.fill("lightgray")
        t = self.font.render(self.text, True, "#000000")
        b.blit(t, (0, 0))
        blits.append((b, self.rect.topleft))
        return blits

    
    def is_clicked(self, mouse_pos: pygame.Vector2):
        if self.rect.collidepoint(mouse_pos):
            self.callback()
    
