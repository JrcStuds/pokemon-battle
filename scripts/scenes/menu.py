import pygame
import assets.config.globals as g
import scripts.scenes as scenes
import scripts.ui as ui



class Menu(scenes.SceneBaseClass):
    def __init__(self):
        super().__init__()

        self.background = "white"

        self.add_elements(
            ui.Text(
                (0, 0),
                "Pokemon Battle",
                "regular"
            ),
            ui.Button(
                lambda: g.scene_manager.change_scene(scenes.Battle()),
                pygame.Rect(0, 15, 50, 20),
                "Start Battle (A)",
                "regular"
            )
        )

    
    def handle_event(self, event):
        if g.keys["a"]:
            g.scene_manager.change_scene(scenes.Battle())