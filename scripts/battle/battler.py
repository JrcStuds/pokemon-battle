import pygame, random
import scripts.scenes as scenes
import scripts.ui as ui



class Battler(scenes.SceneBaseClass):
    def __init__(self, battle, rect: pygame.Rect, pokemon: list):
        super().__init__(rect=rect)
        self.battle = battle

        self.background = "coral"

        self.pokemon = pokemon
        self.active_pokemon = self.pokemon[0]

        self.pokemon_name_text = ui.Text(
            pos=self.rect.move(5, 5).topleft,
            text=self.active_pokemon.name
        )
        self.pokemon_hp_text = ui.Text(
            pos=self.rect.move(5, 15).topleft,
            text=str(self.active_pokemon.hp)
        )
        self.add_elements(self.pokemon_name_text, self.pokemon_hp_text)

    
    def execute_random_move(self, target):
        if not len(self.active_pokemon.moveset):
            raise KeyError(f"pokemon has no moves")

        idx = random.randint(0, len(self.active_pokemon.moveset)-1)
        self.active_pokemon.moveset[idx].execute(target=target)

        return
    

    def update_text(self):
        self.pokemon_name_text.update_text(self.active_pokemon.name)
        self.pokemon_hp_text.update_text(str(round(self.active_pokemon.hp)))