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
                cursor_pos=g.BATTLE_MENU_RECTS["general"][0]
            ),
            ui.Button(
                callback=lambda: menus.DialogueMenu(self.battle, "There's no bag!").enter_state(),
                cursor_pos=g.BATTLE_MENU_RECTS["general"][1]
            ),
            ui.Button(
                callback=lambda: menus.PokemonBattleMenu(self.battle).enter_state(),
                cursor_pos=g.BATTLE_MENU_RECTS["general"][2]
            ),
            ui.Button(
                callback=lambda: menus.DialogueMenu(self.battle, "Can't run!").enter_state(),
                cursor_pos=g.BATTLE_MENU_RECTS["general"][3]
            )
        )

        self.cursor = ui.Cursor(self.elements[0:4], "four_button")

        self.add_elements(
            ui.Image(
                pos=g.BATTLE_MENU_RECTS["general"]["backing"],
                spritesheet="menus",
                name="backing"
            ),
            ui.Image(
                pos=g.BATTLE_MENU_RECTS["general"]["menu"],
                spritesheet="menus",
                name="general"
            ),
            ui.Text(
                pos=g.BATTLE_MENU_RECTS["general"]["text"][0],
                text="What will",
                type="regular",
                col="light_alt"
            ),
            ui.Text(
                pos=g.BATTLE_MENU_RECTS["general"]["text"][1],
                text=f"{self.battle.attacker.active_pokemon.name.upper()} do?",
                type="regular",
                col="light_alt"
            ),
            self.cursor
        )