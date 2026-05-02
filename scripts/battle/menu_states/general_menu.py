import pygame
import assets.config.globals as g
import scripts.ui as ui
import scripts.battle.menu_states as menus
from .menu_base_scene import BattleMenuSceneBaseClass



class GeneralBattleMenu(BattleMenuSceneBaseClass):
    def __init__(self, battle):
        super().__init__(battle=battle)

        self.add_elements(
            ui.Button(
                callback=lambda: menus.FightBattleMenu(self.battle).enter_state(),
                rect=g.GENERAL_MENU_BUTTON_RECTS[0]
            ),
            ui.Button(
                callback=lambda: menus.DialogueMenu(self.battle, "There's no bag!").enter_state(),
                rect=g.GENERAL_MENU_BUTTON_RECTS[1]
            ),
            ui.Button(
                callback=lambda: menus.PokemonBattleMenu(self.battle).enter_state(),
                rect=g.GENERAL_MENU_BUTTON_RECTS[2]
            ),
            ui.Button(
                callback=lambda: menus.DialogueMenu(self.battle, "Can't run!").enter_state(),
                rect=g.GENERAL_MENU_BUTTON_RECTS[3]
            )
        )

        self.cursor = ui.Cursor(self.elements[0:4], "four_button")

        self.add_elements(
            ui.Image(
                pos=(0, 112),
                spritesheet="menus",
                name="backing"
            ),
            ui.Image(
                pos=(120, 112),
                spritesheet="menus",
                name="general"
            ),
            ui.Text(
                pos=(10, 122),
                text="What will",
                type="regular",
                col="light_alt"
            ),
            ui.Text(
                pos=(10, 138),
                text=f"{self.battle.attacker.active_pokemon.name.upper()} do?",
                type="regular",
                col="light_alt"
            ),
            self.cursor
        )