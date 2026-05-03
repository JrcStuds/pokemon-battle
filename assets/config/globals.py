import pygame


FPS = 60
DISPLAY_RECT = pygame.Rect(0, 0, 240, 160)


scene_manager = None
spritesheets = {
    "pokemon": None,
    "text": None,
    "menus": None,
    "backgrounds": None
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


BATTLE_MENU_RECTS = {
    "general": {
        "backing": (0, 112),
        "menu": (120, 112),
        "text": [(10, 122), (10, 138)],
        0: (129, 124),
        1: (185, 124),
        2: (129, 140),
        3: (185, 140),
    },
    "fight": {
        "menu": (0, 112),
        0: [pygame.Rect(16, 120, 0, 0), (9, 122)],
        1: [pygame.Rect(88, 120, 0, 0), (81, 122)],
        2: [pygame.Rect(16, 136, 0, 0), (8, 138)],
        3: [pygame.Rect(88, 136, 0, 0), (81, 138)],
    },
    "pokemon": {
        0: {
            "container": (2, 18),
            "image": (0, 24),
            "name": (32, 35),
            "hp_bar": (17, 57),
            "hp_text": (80, 61)
        },
        1: {
            "container": (88, 9),
            "image": (82, 2),
            "name": (116, 12),
            "hp_bar": (169, 16),
            "hp_text": (232, 21)
        },
        2: {
            "container": (88, 33),
            "image": (82, 26),
            "name": (116, 36),
            "hp_bar": (169, 40),
            "hp_text": (232, 45)
        },
        3: {
            "container": (88, 57),
            "image": (82, 50),
            "name": (116, 60),
            "hp_bar": (169, 64),
            "hp_text": (232, 69)
        },
        4: {
            "container": (88, 81),
            "image": (82, 74),
            "name": (116, 84),
            "hp_bar": (169, 88),
            "hp_text": (232, 93)
        },
        5: {
            "container": (88, 105),
            "image": (82, 98),
            "name": (116, 108),
            "hp_bar": (169, 102),
            "hp_text": (232, 117)
        }
    }
}


DIALOGUE_RECTS = {
    "container": pygame.Rect(0, 96, 240, 64)
}


BATTLER_RECTS = {
    "attacker": {
        "info": (126, 74),
        "sprite": (40, 64),
        "name": (142, 76),
        "hp_bar": (159, 89),
        "hp_text": (221, 94)
    },
    "defender": {
        "info": (13, 16),
        "sprite": (144, 24),
        "name": (20, 18),
        "hp_bar": (37, 31)
    }
}


BACKGROUND_SPRITESHEET_RECT = pygame.Rect(249, 6, 240, 112)


TEXT_COLOUR_PALETTES = {
    "dark": [(96, 96, 96), (208, 208, 200)],
    "light": [(248, 248, 248), (96, 96, 96)],
    "dark_alt": [(64, 64, 64), (216, 208, 176)],
    "light_alt": [(248, 248, 248), (104, 88, 112)]
}


HP_COLOURS = {
    "red_light": (208, 40, 40),
    "red_dark": (128, 0, 0),
    "yellow_light": (248, 224, 56),
    "yellow_dark": (200, 168, 8),
    "green_light": (112, 248, 168),
    "green_dark": (88, 208, 128)
}