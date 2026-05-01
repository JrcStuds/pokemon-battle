import pygame
import assets.config.globals as g
import scripts.scenes as scenes
import scripts.ui as ui



class Menu(scenes.SceneBaseClass):
    def __init__(self):
        super().__init__()

        self.background = "white"

        self.elements.append(ui.Text((0, 0), f"pokemon battle", "dodgerblue"))

        self.elements.append(ui.Button(
            lambda: g.scene_manager.change_scene(scenes.Battle()),
            pygame.Rect(0, 15, 50, 20),
            "start battle (A)"
        ))

        self.elements.append(ui.Image(
            pos=(50, 50),
            type="mini",
            name="charmander"
        ))

    
    def handle_event(self, event):
        if g.keys["a"]:
            g.scene_manager.change_scene(scenes.Battle())