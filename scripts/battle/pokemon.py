import json
import scripts.battle.menu_states as menus
from .move import Move


class Pokemon():
    def __init__(self, battler, name):
        self.name = name
        self.battler = battler

        with open("assets/data/pokemon.json", "r") as file:
            pokemon_db = json.load(file)

        self.level = 1
        self.type = pokemon_db[name]["type"]
        self.max_hp = pokemon_db[name]["hp"]
        self.hp = pokemon_db[name]["hp"]
        self.attack = pokemon_db[name]["attack"]
        self.defense = pokemon_db[name]["defense"]
        self.sp_attack = pokemon_db[name]["sp_attack"]
        self.sp_defense = pokemon_db[name]["sp_defense"]
        self.speed = pokemon_db[name]["speed"]
        self.moveset = [Move(self, move) for move in pokemon_db[name]["moveset"]]


    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0.5 and self.hp != 0:
            self.hp = 0
        return
    

    def switch(self):
        if self.hp == 0:
            menus.DialogueMenu(self.battler.battle, "No HP left!").enter_state()
            return
        
        self.battler.battle.queue_move({
            "type": "switch",
            "battler": self.battler,
            "pokemon_idx": self.battler.pokemon.index(self)
        })