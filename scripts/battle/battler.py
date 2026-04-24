import pygame
import scripts.scenes as scenes
import scripts.ui as ui



class Battler(scenes.SceneBaseClass):
    def __init__(self, battle, rect: pygame.Rect, id: int, pokemon: list):
        super().__init__(rect=rect)
        self.battle = battle

        self.id = id
        self.pokemon = pokemon
        self.active_pokemon = self.pokemon[0]

        self.add_elements(
            ui.Text((0, self.id*20+20), self.pokemon[0].name),
            ui.Text((100, self.id*20+20), str(self.pokemon[0].hp))
        )