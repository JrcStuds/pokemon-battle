import pygame
import assets.config.globals as g
import scripts.ui as ui
import scripts.battle.menu_states as menus
from .menu_base_scene import BattleMenuSceneBaseClass



class PokemonBattleMenu(BattleMenuSceneBaseClass):
    def __init__(self, battle):
        super().__init__(battle=battle)

        self.background = "white"

        self.add_elements(ui.Button(
            callback=lambda: menus.DialogueMenu(self.battle, "Nothing Happened...").enter_state(),
            rect=pygame.Rect(5, 20, 100, 20),
            text=self.battle.attacker.active_pokemon.name
        ))
        i, j = 0, 0
        while i <= 4:
            print(j, len(self.battle.attacker.pokemon))
            if self.battle.attacker.pokemon.index(self.battle.attacker.active_pokemon) == i:
                j += 1
            if len(self.battle.attacker.pokemon) <= j:
                text = ""
            else:
                text = self.battle.attacker.pokemon[j].name
            self.add_elements(ui.Button(
                callback=lambda: menus.DialogueMenu(self.battle, "Nothing Happened...").enter_state(),
                rect=pygame.Rect(110, 25*i+5, 100, 20),
                text=text
            ))
            i, j = i+1, j+1
        
        self.cursor = ui.Cursor(self.elements[0:6], "pokemon_menu")
        self.add_elements(self.cursor)

        self.header = ui.Text((5, 5), "POKEMON MENU")
        self.add_elements(self.header)
    

    def handle_event(self, event):
        super().handle_event(event)

        if g.keys["b"]:
            self.exit_state()

    
    def update(self, dt):
        return super().update(dt)