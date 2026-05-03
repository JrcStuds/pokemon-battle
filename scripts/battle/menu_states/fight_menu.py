import pygame
import assets.config.globals as g
import scripts.ui as ui
import scripts.battle.menu_states as menu_states
from .menu_base_scene import BattleMenuSceneBaseClass



class FightBattleMenu(BattleMenuSceneBaseClass):
    def __init__(self, battle):
        super().__init__(battle=battle)

        self.add_elements(
            ui.Image(
                pos=g.BATTLE_MENU_RECTS["fight"]["menu"],
                spritesheet="menus",
                name="fight"
            )
        )

        for i in range(4):
            if len(self.battle.attacker.active_pokemon.moveset) <= i:  # if there aren't enough moves in the moveset
                self.add_elements(ui.Button(
                    callback=lambda: None,
                    rect=g.BATTLE_MENU_RECTS["fight"][i][0],
                    cursor_pos=g.BATTLE_MENU_RECTS["fight"][i][1],
                ))
                continue
            
            # callback calls for the move to be executed
            self.add_elements(ui.Button(
                callback=lambda i=i: self.battle.attacker.active_pokemon.moveset[i].execute(target=self.battle.defender),
                rect=g.BATTLE_MENU_RECTS["fight"][i][0],
                cursor_pos=g.BATTLE_MENU_RECTS["fight"][i][1],
                text=self.battle.attacker.active_pokemon.moveset[i].name,
            ))
        self.cursor = ui.Cursor(self.elements[1:5], "four_button")
        self.add_elements(self.cursor)


    def handle_event(self, event):
        super().handle_event(event)
        
        if g.keys["b"]:
            self.exit_state()