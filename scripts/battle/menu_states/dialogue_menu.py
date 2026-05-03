import pygame
import assets.config.globals as g
import scripts.ui as ui
import scripts.battle.menu_states as menu_states
from .menu_base_scene import BattleMenuSceneBaseClass



class DialogueMenu(BattleMenuSceneBaseClass):
    def __init__(self, battle, text):
        super().__init__(battle=battle, background=None)
        self.pos = g.BATTLE_MENU_RECTS["dialogue"]["container"]

        self.text = ui.Text(
            pos=g.BATTLE_MENU_RECTS["dialogue"]["text"],
            text=text,
            col="light_alt"
        )
        self.add_elements(
            ui.Image(
                pos=self.pos,
                spritesheet="menus",
                name="backing"
            ),
            ui.Image(
                pos=g.BATTLE_MENU_RECTS["dialogue"]["cursor"],
                spritesheet="menus",
                name="dialogue_cursor"
            ),
            self.text
        )
    

    def handle_event(self, event):
        super().handle_event(event)

        if g.keys["a"]:
            self.exit_state()   # after dialogue is passed, the one under it will show (in the stack)