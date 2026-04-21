import json



with open("pokemon.json", "r") as file:
    pokemon_db = json.load(file)
with open("moves.json", "r") as file:
    moves_db = json.load(file)


class Pokemon():
    def __init__(self, name):
        self.name = name
        self.hp = pokemon_db[name]["hp"]
        self.type = pokemon_db[name]["type"]
        self.attack = pokemon_db[name]["attack"]
        self.defense = pokemon_db[name]["defense"]
        self.moveset = pokemon_db[name]["moveset"]



class Battle():
    def __init__(self):
        self.player_one = Pokemon("charmander")
        self.player_two = Pokemon("bulbasaur")


    def move(self, attacker: str, defender: str, move_idx: int):
        attacker = self.player_one if attacker == "player_one" else self.player_two
        defender = self.player_one if defender == "player_one" else self.player_two

        if len(attacker.moveset) <= move_idx:
            return "invalid move index"
        
        move = moves_db[attacker.moveset[move_idx]]

        defender.hp -= move["power"]
        return



battle = Battle()

print(battle.player_one.name, battle.player_one.hp, battle.player_two.name, battle.player_two.hp)

battle.move("player_one", "player_two", 0)

print(battle.player_one.name, battle.player_one.hp, battle.player_two.name, battle.player_two.hp, "move used:", battle.player_one.moveset[0])