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
            lambda: g.scene_manager.change_scene(g.scenes["battle"]),
            pygame.Rect(0, 15, 50, 20),
            "start battle"
        ))

    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                g.scene_manager.change_scene(g.scenes["battle"])
        
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 1:
                g.scene_manager.change_scene(g.scenes["battle"])