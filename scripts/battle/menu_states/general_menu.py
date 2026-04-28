import pygame
import assets.config.globals as g
import scripts.ui as ui
import scripts.battle.menu_states as menu_states
from .four_button_menu import FourButtonMenuBaseClass



class GeneralBattleMenu(FourButtonMenuBaseClass):
    def __init__(self, battle):
        super().__init__(battle=battle)

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

        self.init_cursor()


    def handle_event(self, event):
        super().handle_event(event)