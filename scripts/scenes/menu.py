import pygame
import assets.config.globals as g
import scripts.scenes as scenes
import scripts.ui as ui



class Menu(scenes.SceneBaseClass):
    def __init__(self, background = "white"):
        super().__init__(background=background)

        self.add_elements(
            ui.Text(
                pos=(0, 0),
                text="Pokemon Battle"
            ),
            ui.Text(
                pos=(0, 15),
                text="Start Battle (A)"
            )
        )

    
    def handle_event(self, event):
        if g.keys["a"]:
            g.scene_manager.change_scene(scenes.Battle())