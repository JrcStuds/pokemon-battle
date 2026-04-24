import pygame, random
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

    
    def execute_random_move(self, target):
        if not len(self.active_pokemon.moveset):
            raise KeyError(f"pokemon has no moves")

        idx = random.randint(0, len(self.active_pokemon.moveset)-1)
        self.active_pokemon.moveset[idx].execute(user=self.active_pokemon, target=target)

        return