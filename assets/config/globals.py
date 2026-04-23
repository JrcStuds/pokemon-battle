import pygame


FPS = 60
DISPLAY_RECT = pygame.Rect(0, 0, 240, 160)


FOUR_BUTTON_RECTS = {
    "margin": 10,
    "container_rect": pygame.Rect(128, 96, 112, 64),
    "topleft": pygame.Rect(133, 101, 46, 22),
    "topright": pygame.Rect(189, 101, 46, 22),
    "bottomleft": pygame.Rect(133, 133, 46, 22),
    "bottomright": pygame.Rect(189, 133, 46, 22),
}


scene_manager = None
scenes = {}