import pygame


FPS = 60
DISPLAY_RECT = pygame.Rect(0, 0, 240, 160)


KEYS = {
    "up": [pygame.K_UP, pygame.K_w],
    "down": [pygame.K_DOWN, pygame.K_s],
    "left": [pygame.K_LEFT, pygame.K_a],
    "right": [pygame.K_RIGHT, pygame.K_d],
    "a": [pygame.K_x, pygame.K_RETURN],
    "b": [pygame.K_z, pygame.K_RSHIFT],
}


FOUR_BUTTON_RECTS = {
    "margin": 10,
    "container": pygame.Rect(128, 96, 112, 64),
    0: pygame.Rect(133, 101, 46, 22),
    1: pygame.Rect(189, 101, 46, 22),
    2: pygame.Rect(133, 133, 46, 22),
    3: pygame.Rect(189, 133, 46, 22),
}


DIALOGUE_RECTS = {
    "container": pygame.Rect(0, 96, 240, 64)
}


POKEMON_INFO_RECTS = {
    "opponent": pygame.Rect(30, 10, 80, 30),
    "player": pygame.Rect(130, 60, 80, 30)
}


scene_manager = None
scenes = {}