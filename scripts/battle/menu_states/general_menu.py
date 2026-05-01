import pygame
import assets.config.globals as g
import scripts.ui as ui
import scripts.battle.menu_states as menus
from .menu_base_scene import BattleMenuSceneBaseClass



class GeneralBattleMenu(BattleMenuSceneBaseClass):
    def __init__(self, battle):
        super().__init__(battle=battle)

        self.rect = g.FOUR_BUTTON_RECTS["container"]
        self.background = "dodgerblue"

        self.add_elements(
            ui.Button(
                lambda: menus.FightBattleMenu(self.battle).enter_state(),
                g.FOUR_BUTTON_RECTS[0],
                "Fight"
            ),
            ui.Button(
                lambda: menus.PokemonBattleMenu(self.battle).enter_state(),
                g.FOUR_BUTTON_RECTS[1],
                "PKMN"
            ),
            ui.Button(
                lambda: menus.DialogueMenu(self.battle, "There's no bag!").enter_state(),
                g.FOUR_BUTTON_RECTS[2],
                "Items"
            ),
            ui.Button(
                lambda: menus.DialogueMenu(self.battle, "Can't run!").enter_state(),
                g.FOUR_BUTTON_RECTS[3],
                "Run"
            )
        )
        self.cursor = ui.Cursor(self.elements[0:4], "four_button")
        self.add_elements(self.cursor)