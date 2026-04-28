import pygame
import assets.config.globals as g
import scripts.ui as ui
import scripts.battle.menu_states as menu_states
from .menu_base_scene import BattleMenuSceneBaseClass



class DialogueMenu(BattleMenuSceneBaseClass):
    def __init__(self, battle, text):
        super().__init__(battle)

        self.rect = g.DIALOGUE_RECTS["container"]
        self.background = "lightpink"

        self.text = ui.Text(pos=self.rect.move(5, 5).topleft, text=text)
        self.add_elements(self.text)
    

    def handle_event(self, event):
        super().handle_event(event)

        if event.type == pygame.KEYDOWN:
            if event.key in g.KEYS["a"]:
                self.exit_state()