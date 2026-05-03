import pygame
import assets.config.globals as g
import scripts.scenes as scenes
import scripts.ui as ui



class Menu(scenes.SceneBaseClass):
    def __init__(self):
        super().__init__(background=ui.image.create_surface_from_spritesheet("intro", "tall_grass"))

        self.add_elements(
            ui.Text(
                pos=(120, 90),
                text="Pokemon Battle",
                alignment="center",
                col="light_alt"
            ),
            ui.Text(
                pos=(120, 105),
                text="Start Battle (A)",
                alignment="center",
                col="light_alt"
            )
        )

    
    def handle_event(self, event):
        if g.keys["a"]:
            g.scene_manager.change_scene(scenes.Battle())