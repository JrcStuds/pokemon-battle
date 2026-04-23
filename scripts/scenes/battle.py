import pygame
import assets.config.globals as g
import scripts.scenes as scenes
import scripts.ui as ui
import scripts.battle as battle
from scripts.battle.menu_states.general_menu import GeneralBattleMenu



class Battle(scenes.SceneBaseClass):
    def __init__(self):
        super().__init__()

        self.menu_stack = []

        self.background = "white"
        self.elements.append(ui.Text((0, 0), "Battle", "dodgerblue"))
        
        self.player = battle.Battler(pygame.Rect(0, 20, g.DISPLAY_RECT.width, 20), 0, [ battle.Pokemon("Charmander") ])
        self.opponent = battle.Battler(pygame.Rect(0, 40, g.DISPLAY_RECT.width, 20), 1, [ battle.Pokemon("Bulbasaur") ])

        self.add_elements(self.player, self.opponent)

        GeneralBattleMenu(battle=self).enter_state()
    

    def handle_event(self, event):
        if len(self.menu_stack):
            self.menu_stack[-1].handle_event(event)