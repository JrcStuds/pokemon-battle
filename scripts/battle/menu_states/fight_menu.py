import pygame
import assets.config.globals as g
import scripts.ui as ui
import scripts.scenes as scenes



class FightBattleMenu(scenes.BattleMenuSceneBaseClass):
    def __init__(self, battle):
        super().__init__(battle=battle)

        self.rect = pygame.Rect(128, 96, 112, 64)
        self.background = "dodgerblue"

        self.add_elements(
            ui.Button(
                lambda: print("move1"),
                g.FOUR_BUTTON_RECTS["topleft"],
                "move1"
            ),
            ui.Button(
                lambda: print("move2"),
                g.FOUR_BUTTON_RECTS["topright"],
                "move2"
            ),
            ui.Button(
                lambda: print("move3"),
                g.FOUR_BUTTON_RECTS["bottomleft"],
                "move3"
            ),
            ui.Button(
                lambda: print("move4"),
                g.FOUR_BUTTON_RECTS["bottomright"],
                "move4"
            )
        )


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for element in self.elements:
                if element.rect.collidepoint(event.pos):
                    element.click()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                self.exit_state()