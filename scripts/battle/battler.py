import pygame
import scripts.scenes as scenes
import scripts.ui as ui



class Battler(scenes.SceneBaseClass):
    def __init__(self, rect: pygame.Rect, id: int, pokemon: list):
        super().__init__(rect=rect)

        self.id = id
        self.pokemon = pokemon

        self.add_elements(
            ui.Text((0, 0), self.pokemon[0].name),
            ui.Text((100, 0), str(self.pokemon[0].hp))
        )