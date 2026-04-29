import pygame
import assets.config.globals as g
import scripts.ui as ui
import scripts.battle.menu_states as menu_states
from .menu_base_scene import BattleMenuSceneBaseClass



class GeneralBattleMenu(BattleMenuSceneBaseClass):
    def __init__(self, battle):
        super().__init__(battle=battle)

        self.rect = g.FOUR_BUTTON_RECTS["container"]
        self.background = "dodgerblue"

        self.add_elements(
            ui.Button(
                lambda: menu_states.FightBattleMenu(battle=self.battle).enter_state(),
                g.FOUR_BUTTON_RECTS[0],
                "fight"
            ),
            ui.Button(
                lambda: print("pkmn"),
                g.FOUR_BUTTON_RECTS[1],
                "pkmn"
            ),
            ui.Button(
                lambda: print("items"),
                g.FOUR_BUTTON_RECTS[2],
                "items"
            ),
            ui.Button(
                lambda: print("run"),
                g.FOUR_BUTTON_RECTS[3],
                "run"
            )
        )
        self.cursor = ui.Cursor(self.elements[0:4], "four_button")
        self.add_elements(self.cursor)