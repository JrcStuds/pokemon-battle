import pygame
import assets.config.globals as g
import scripts.ui as ui
import scripts.battle.menu_states as menus



class FightBattleMenu(menus.BattleMenuSceneBaseClass):
    def __init__(self, battle):
        super().__init__(battle=battle)

        self.rect = g.FOUR_BUTTON_RECTS["container_rect"]
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

        self.cursor_elements = {
            0: self.elements[0],
            1: self.elements[1],
            2: self.elements[2],
            3: self.elements[3],
        }
        self.cursor_idx = 0
        self.cursor = ui.Cursor(pos=self.cursor_elements[self.cursor_idx].rect.center, visible=True)
        self.add_elements(self.cursor)


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for element in self.elements:
                if element.rect.collidepoint(event.pos):
                    element.click()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                self.exit_state()
            if event.key == pygame.K_x and hasattr(self.cursor_elements[self.cursor_idx], "click"):
                self.cursor_elements[self.cursor_idx].click()
            if event.key == pygame.K_UP and self.cursor_idx >= 2:
                self.cursor_idx -= 2
                self.cursor.pos = self.cursor_elements[self.cursor_idx].rect.center
            if event.key == pygame.K_DOWN and self.cursor_idx <= 1:
                self.cursor_idx += 2
                self.cursor.pos = self.cursor_elements[self.cursor_idx].rect.center
            if event.key == pygame.K_LEFT and self.cursor_idx % 2 == 1:
                self.cursor_idx -= 1
                self.cursor.pos = self.cursor_elements[self.cursor_idx].rect.center
            if event.key == pygame.K_RIGHT and self.cursor_idx % 2 == 0:
                self.cursor_idx += 1
                self.cursor.pos = self.cursor_elements[self.cursor_idx].rect.center