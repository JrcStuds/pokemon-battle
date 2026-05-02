import pygame, random
import assets.config.globals as g
import scripts.scenes as scenes
import scripts.ui as ui
from .pokemon import Pokemon



class Battler(scenes.SceneBaseClass):
    def __init__(self, battle, pokemon: list, attacker: bool):
        super().__init__()
        self.battle = battle

        self.pokemon = [Pokemon(self, name) for name in pokemon]
        self.active_pokemon = self.pokemon[0]
        self.position = "attacker" if attacker else "defender"

        self.sprite = ui.Image(
            pos=g.BATTLER_RECTS[self.position]["sprite"],
            spritesheet="pokemon",
            type="back" if self.position == "attacker" else "front",
            name=self.active_pokemon.name
        )
        self.info = ui.Image(
            pos=g.BATTLER_RECTS[self.position]["info"],
            spritesheet="menus",
            name=f"{self.position}_info"
        )
        self.name = ui.Text(
            pos=g.BATTLER_RECTS[self.position]["name"],
            text=self.active_pokemon.name,
            type="small",
            col="dark_alt"
        )
        self.add_elements(self.sprite, self.info, self.name)

    
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
            spritesheet="pokemon",
            type=self.sprite_type,
            name=self.active_pokemon.name
        )
        self.add_elements(self.pokemon_sprite)