import pygame


FPS = 60
DISPLAY_RECT = pygame.Rect(0, 0, 240, 160)


scene_manager = None
spritesheets = {
    "pokemon": None,
    "text": None,
    "menus": None
}


keys = {}
CONTROLS = {
    "up": [pygame.K_UP, pygame.K_w],         # Joy UP
    "down": [pygame.K_DOWN, pygame.K_s],     # Joy DOWN
    "left": [pygame.K_LEFT, pygame.K_a],     # Joy LEFT
    "right": [pygame.K_RIGHT, pygame.K_d],   # Joy RIGHT
    "a": [pygame.K_x, pygame.K_RETURN],
    "b": [pygame.K_z, pygame.K_RSHIFT],
}


GENERAL_MENU_BUTTON_RECTS = {
    "margin": 10,
    "container": pygame.Rect(128, 96, 112, 64),
    0: pygame.Rect(129, 124, 0, 0),
    1: pygame.Rect(185, 124, 0, 0),
    2: pygame.Rect(129, 140, 0, 0),
    3: pygame.Rect(185, 140, 0, 0),
}


DIALOGUE_RECTS = {
    "container": pygame.Rect(0, 96, 240, 64)
}


BATTLER_RECTS = {
    "attacker": {
        "info": (126, 74),
        "sprite": (40, 64),
        "name": (142, 76)
    },
    "defender": {
        "info": (13, 16),
        "sprite": (144, 24),
        "name": (20, 18)
    }
}


BACKGROUND_SPRITESHEET_RECT = pygame.Rect(249, 6, 240, 112)


TEXT_COLOUR_PALETTES = {
    "dark": [(96, 96, 96), (208, 208, 200)],
    "light": [(248, 248, 248), (96, 96, 96)],
    "dark_alt": [(64, 64, 64), (216, 208, 176)],
    "light_alt": [(248, 248, 248), (104, 88, 112)]
}