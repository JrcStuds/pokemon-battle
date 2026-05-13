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
        self.power = moves_db[name]["power"]
        self.lv = moves_db[name]["lv"]


    # appends self alongside target to the battle's queued moves for execution
    def execute(self, target):
        move = {
            "type": "move",
            "move": self,
            "target": target
        }
        self.pokemon.battler.battle.queue_move(move)