import pygame
import scripts.ui as ui



class Battler(ui.Container):
    def __init__(self, id: int, pokemon: list):
        super().__init__()

        self.id = id
        self.pokemon = pokemon

        self.add_elements(
            ui.Text((0, (self.id+1)*20), self.pokemon[0].name),
            ui.Text((100, (self.id+1)*20), str(self.pokemon[0].hp))
        )