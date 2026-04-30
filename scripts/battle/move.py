import json


class Move():
    def __init__(self, pokemon, name):
        self.pokemon = pokemon
        self.name = name

        with open("assets/data/moves.json", "r") as file:
            moves_db = json.load(file)

        self.type = moves_db[name]["type"]
        self.category = moves_db[name]["category"]
        self.accuracy = moves_db[name]["accuracy"]
        self.pp = moves_db[name]["pp"]
        self.power = moves_db[name]["power"]


    def execute(self, target):
        move = {
            "type": "move",
            "move": self,
            "target": target
        }
        self.pokemon.battler.battle.queue_move(move)