import pygame
import assets.config.globals as g
import scripts.scenes as scenes
import scripts.ui as ui
import scripts.battle as battle
from scripts.battle.menu_states.general_menu import GeneralBattleMenu
from scripts.battle.menu_states.fight_menu import FightBattleMenu



class Battle(scenes.SceneBaseClass):
    def __init__(self):
        super().__init__()

        self.menu_stack = []

        self.background = "white"
        self.elements.append(ui.Text((0, 0), "Battle", "dodgerblue"))
        
        self.player = battle.Battler(self, pygame.Rect(0, 20, g.DISPLAY_RECT.width, 20), 0, [ battle.Pokemon(self, "Charmander") ])
        self.opponent = battle.Battler(self, pygame.Rect(0, 40, g.DISPLAY_RECT.width, 20), 1, [ battle.Pokemon(self, "Bulbasaur") ])
        self.current_attacker = self.player

        self.add_elements(self.player, self.opponent)

        GeneralBattleMenu(battle=self).enter_state()
    

    def handle_event(self, event):
        if len(self.menu_stack):
            self.menu_stack[-1].handle_event(event)

    
    def swap_attacker(self):
        print(self.current_attacker.id)
        if self.current_attacker == self.player:
            self.current_attacker = self.opponent
        else:
            self.current_attacker = self.player
        print(self.current_attacker.id)