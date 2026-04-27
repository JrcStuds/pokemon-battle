import pygame
import assets.config.globals as g
import scripts.ui as ui
import scripts.battle.menu_states as menus
from .four_button_menu import FourButtonMenuBaseClass



class FightBattleMenu(FourButtonMenuBaseClass):
    def __init__(self, battle):
        super().__init__(battle=battle)

        for i in range(4):
            if len(self.battle.attacker.active_pokemon.moveset) <= i:
                self.add_elements(ui.Button(
                    callback=lambda i=i: print(f"move{i}"),
                    rect=g.FOUR_BUTTON_RECTS[i]
                ))
                continue
                
            self.add_elements(ui.Button(
                callback=lambda i=i: self.battle.attacker.active_pokemon.moveset[i].execute(target=self.battle.defender.active_pokemon),
                rect=g.FOUR_BUTTON_RECTS[i],
                text=self.battle.attacker.active_pokemon.moveset[i].name
            ))

        self.init_cursor()


    def handle_event(self, event):
        super().handle_event(event)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                self.exit_state()