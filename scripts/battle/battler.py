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
        self.hp_bar = ui.HpBar(
            pos=g.BATTLER_RECTS[self.position]["hp_bar"],
            value=round(self.active_pokemon.hp / self.active_pokemon.max_hp * 48)
        )
        self.add_elements(self.sprite, self.info, self.name, self.hp_bar)

        if self.position == "attacker":
            self.hp_text = ui.Text(
                pos=g.BATTLER_RECTS[self.position]["hp_text"],
                text=f"{round(self.active_pokemon.hp)}/{self.active_pokemon.max_hp}",
                type="small",
                col="dark_alt",
                alignment="right"
            )
            self.add_elements(self.hp_text)

    
    def execute_random_move(self, target):
        if not len(self.active_pokemon.moveset):
            raise KeyError(f"pokemon has no moves")

        idx = random.randint(0, len(self.active_pokemon.moveset)-1)   # pick random index from moveset
        self.active_pokemon.moveset[idx].execute(target=target)

        return
    

    def update_info(self):
        self.name.update_text(self.active_pokemon.name)
        self.hp_bar.update_value(round(self.active_pokemon.hp / self.active_pokemon.max_hp * 48))

        self.elements.remove(self.sprite)
        self.sprite = ui.Image(
            pos=g.BATTLER_RECTS[self.position]["sprite"],
            spritesheet="pokemon",
            type="back" if self.position == "attacker" else "front",
            name=self.active_pokemon.name
        )
        self.add_elements(self.sprite)

        if hasattr(self, "hp_text"):
            self.hp_text.update_text(f"{round(self.active_pokemon.hp)}/{self.active_pokemon.max_hp}")