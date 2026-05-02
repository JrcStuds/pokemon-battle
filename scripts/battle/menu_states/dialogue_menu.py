import pygame
import assets.config.globals as g
import scripts.ui as ui
import scripts.battle.menu_states as menu_states
from .menu_base_scene import BattleMenuSceneBaseClass



class DialogueMenu(BattleMenuSceneBaseClass):
    def __init__(self, battle, text, *args):
        super().__init__(battle)

        self.rect = g.DIALOGUE_RECTS["container"]
        self.background = "lightpink"
        if "empty" in args:
            self.background = None

        self.text = ui.Text(pos=self.rect.move(5, 5).topleft, text=text, type="regular")
        self.add_elements(self.text)
    

    def handle_event(self, event):
        super().handle_event(event)

        if g.keys["a"]:
            self.exit_state()   # after dialogue is passed, the one under it will show (in the stack)