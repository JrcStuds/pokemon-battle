import pygame
import assets.config.globals as g
import scripts.ui as ui
import scripts.scenes as scenes

from .fight_menu import FightBattleMenu



class GeneralBattleMenu(scenes.BattleMenuSceneBaseClass):
    def __init__(self, battle):
        super().__init__(battle=battle)

        self.rect = pygame.Rect(128, 96, 112, 64)
        self.background = "dodgerblue"

        self.button_margin = 10
        self.button_size = pygame.Vector2(self.rect.width/2-self.button_margin, self.rect.height/2-self.button_margin)
        self.add_elements(
            ui.Button(
                lambda: FightBattleMenu(battle=self.battle).enter_state(),
                g.FOUR_BUTTON_RECTS["topleft"],
                "fight"
            ),
            ui.Button(
                lambda: print("pkmn"),
                g.FOUR_BUTTON_RECTS["topright"],
                "pkmn"
            ),
            ui.Button(
                lambda: print("items"),
                g.FOUR_BUTTON_RECTS["bottomleft"],
                "items"
            ),
            ui.Button(
                lambda: print("run"),
                g.FOUR_BUTTON_RECTS["bottomright"],
                "run"
            )
        )


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for element in self.elements:
                if element.rect.collidepoint(event.pos):
                    element.click()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                g.scene_manager.change_scene(g.scenes["menu"])