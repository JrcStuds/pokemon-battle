import pygame, random
import assets.config.globals as g
import scripts.scenes as scenes
import scripts.ui as ui
from .pokemon import Pokemon



class Battler(scenes.SceneBaseClass):
    def __init__(self, battle, rect: pygame.Rect, pokemon: list):
        super().__init__(rect=rect)
        self.battle = battle
        self.rect = rect
        self.background = "coral"

        self.pokemon = [Pokemon(self, name) for name in pokemon]
        self.active_pokemon = self.pokemon[0]

        self.sprite_type = "front" if self.rect == g.POKEMON_INFO_RECTS["opponent"] else "back"
        self.pokemon_sprite = ui.Image(
            pos=g.POKEMON_INFO_RECTS["sprite_"+self.sprite_type],
            type=self.sprite_type,
            name=self.active_pokemon.name
        )
        self.pokemon_name_text = ui.Text(
            pos=self.rect.move(5, 5).topleft,
            text=self.active_pokemon.name
        )
        self.pokemon_hp_text = ui.Text(
            pos=self.rect.move(5, 15).topleft,
            text=str(self.active_pokemon.hp)
        )
        self.add_elements(self.pokemon_sprite, self.pokemon_name_text, self.pokemon_hp_text)

    
    def execute_random_move(self, target):
        if not len(self.active_pokemon.moveset):
            raise KeyError(f"pokemon has no moves")

        idx = random.randint(0, len(self.active_pokemon.moveset)-1)   # pick random index from moveset
        self.active_pokemon.moveset[idx].execute(target=target)

        return
    

    def update_text(self):
        hp = round(self.active_pokemon.hp) if round(self.active_pokemon.hp) >= 0.5 else 0   # clamp hp above 0
        self.pokemon_hp_text.update_text(str(hp))
        self.pokemon_name_text.update_text(self.active_pokemon.name)

        self.elements.remove(self.pokemon_sprite)
        self.pokemon_sprite = ui.Image(
            pos=g.POKEMON_INFO_RECTS["sprite_"+self.sprite_type],
            type=self.sprite_type,
            name=self.active_pokemon.name
        )
        self.add_elements(self.pokemon_sprite)