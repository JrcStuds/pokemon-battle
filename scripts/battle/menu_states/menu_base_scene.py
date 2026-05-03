import pygame
import assets.config.globals as g
import scripts.scenes as scenes



class BattleMenuSceneBaseClass(scenes.SceneBaseClass):
    def __init__(self, battle, rect = g.DISPLAY_RECT, background = None):
        super().__init__(rect=rect, background=background)
        self.battle = battle

    def enter_state(self):
        self.battle.menu_stack.append(self)
    
    def exit_state(self):
        self.battle.menu_stack.pop()