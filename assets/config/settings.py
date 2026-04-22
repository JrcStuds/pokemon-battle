import pygame


FPS = 60
DISPLAY_SIZE = (240, 160)
DISPLAY_RECT = pygame.Rect(0, 0, DISPLAY_SIZE[0], DISPLAY_SIZE[1])


scene_manager = None
scenes = {}