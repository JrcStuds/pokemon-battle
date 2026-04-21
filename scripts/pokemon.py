import json
from .move import Move


class Pokemon():
    def __init__(self, name):
        self.name = name

        with open("data/databases/pokemon.json", "r") as file:
            pokemon_db = json.load(file)

        self.type = pokemon_db[name]["type"]
        self.hp = pokemon_db[name]["hp"]
        self.attack = pokemon_db[name]["attack"]
        self.defense = pokemon_db[name]["defense"]
        self.sp_attack = pokemon_db[name]["sp_attack"]
        self.sp_defense = pokemon_db[name]["sp_defense"]
        self.speed = pokemon_db[name]["speed"]
        self.moveset = [Move(move) for move in pokemon_db[name]["moveset"]]