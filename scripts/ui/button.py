import pygame
import assets.config.settings as settings



class Button():
    def __init__( self, callback, rect: pygame.Rect, text: str = None):
        self.font = pygame.font.SysFont("arial", 8)

        self.callback = callback
        self.rect = rect
        self.text = self.font.render(text, False, "black")


    def draw(self) -> list:
        blits = []

        surface = pygame.Surface(self.rect.size)
        surface.fill("lightgray")

        surface.blit(self.text)

        blits.append((surface, self.rect.topleft))
        return blits

    
    def is_clicked(self, mouse_pos: pygame.Vector2):
        if self.rect.collidepoint(mouse_pos):
            self.callback()
    
