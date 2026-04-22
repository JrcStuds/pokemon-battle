import pygame
import assets.config.settings as s
import scripts.ui as ui



class Menu(ui.SceneBaseClass):
    def __init__(self):
        super().__init__()

        self.background = "white"

        self.elements.append(ui.Text((0, 0), f"pokemon battle", "dodgerblue"))

        self.elements.append(ui.Button(
            lambda: s.scene_manager.change_scene(s.scenes["battle"]),
            pygame.Rect(0, 15, 50, 20),
            "start battle"
        ))