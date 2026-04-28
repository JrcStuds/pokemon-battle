import pygame
import assets.config.globals as g
import scripts.scenes as scenes
import scripts.ui as ui



class GameEnd(scenes.SceneBaseClass):
    def __init__(self, winner: str):
        super().__init__()
        self.background = "white"

        self.add_elements(
            ui.Text(
                pos=(5, 5),
                text=f"{winner} wins!"
            ),
            ui.Text(
                pos=(5, 20),
                text="Press A to go back to the main menu"
            )
        )
    

    def handle_event(self, event):
        if g.keys["a"] or g.keys["b"]:
            g.scene_manager.change_scene(scenes.Menu())