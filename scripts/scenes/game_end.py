import pygame
import assets.config.globals as g
import scripts.scenes as scenes
import scripts.ui as ui



class GameEnd(scenes.SceneBaseClass):
    def __init__(self, winner: str, background = "white"):
        super().__init__(background=background)

        self.add_elements(
            ui.Text(
                pos=(5, 5),
                text=f"{winner} wins!",
                type="regular"
            ),
            ui.Text(
                pos=(5, 20),
                text="Press A to go back to the main menu",
                type="regular"
            )
        )
    

    def handle_event(self, event):
        if g.keys["a"] or g.keys["b"]:
            g.scene_manager.change_scene(scenes.Menu())