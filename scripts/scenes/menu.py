import pygame
from scripts.ui.scene import SceneBaseClass
from scripts.ui.text import Text
from scripts.ui.button import Button



class Menu(SceneBaseClass):
    def __init__(self, game, header: str = None):
        super().__init__()
        self.game = game

        self.background = "#ffffff"

        if header: self.elements.append(Text((0, 0), header))

        self.elements.append(Button(
            lambda: game.change_scene("menu", "random"),
            pygame.Rect(100, 100, 50, 20),
            "change scene"
        ))