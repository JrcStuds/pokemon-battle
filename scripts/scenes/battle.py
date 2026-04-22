import pygame
import scripts.ui as ui
import assets.config.settings as s
from scripts.battle.pokemon import Pokemon
from scripts.battle.battler import Battler



class Battle(ui.SceneBaseClass):
    def __init__(self):
        super().__init__()

        self.background = "white"
        self.elements.append(ui.Text((0, 0), "Battle", "dodgerblue"))
        
        self.player = Battler(0, [ Pokemon("Charmander") ])
        self.opponent = Battler(1, [ Pokemon("Bulbasaur") ])

        self.add_elements(self.player, self.opponent)
        self.add_elements(ui.Button(
            lambda: s.scene_manager.change_scene(s.scenes["menu"]),
            pygame.Rect(0, 60, 50, 20),
            "back to menu"
        ))