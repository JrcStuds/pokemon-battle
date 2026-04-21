import json, math



with open("pokemon.json", "r") as file:
    pokemon_db = json.load(file)
with open("moves.json", "r") as file:
    moves_db = json.load(file)



class Move():
    def __init__(self, name):
        self.name = name
        self.type = moves_db[name]["type"]
        self.category = moves_db[name]["category"]
        self.accuracy = moves_db[name]["accuracy"]
        self.pp = moves_db[name]["pp"]
        self.power = moves_db[name]["power"]


    def execute(self, user, target):
        atk_stat = user.attack if self.category == "physical" else user.sp_attack
        def_stat = target.defense if self.category == "physical" else target.sp_defense
        target.hp -= (((2/5)+2)*self.power*(atk_stat/def_stat))/50+2



class Pokemon():
    def __init__(self, name):
        self.name = name
        self.type = pokemon_db[name]["type"]
        self.hp = pokemon_db[name]["hp"]
        self.attack = pokemon_db[name]["attack"]
        self.defense = pokemon_db[name]["defense"]
        self.sp_attack = pokemon_db[name]["sp_attack"]
        self.sp_defense = pokemon_db[name]["sp_defense"]
        self.speed = pokemon_db[name]["speed"]
        self.moveset = [Move(move) for move in pokemon_db[name]["moveset"]]



class Battler():
    def __init__(self, pokemon: list):
        self.pokemon = [Pokemon(name) for name in pokemon]



class Battle():
    def __init__(self):
        self.player_one = Battler(pokemon=["Charmander"])
        self.player_two = Battler(pokemon=["Bulbasaur"])



battle = Battle()

turn = 1
running = True
while running:
    attacker = battle.player_one.pokemon[0] if turn == 1 else battle.player_two.pokemon[0]
    defender = battle.player_one.pokemon[0] if turn == 2 else battle.player_two.pokemon[0]


    if round(attacker.hp) <= 0:
        print(f"{defender.name} Wins!")
        running = False
        continue


    print(f"Attacker: {attacker.name}, HP: {round(attacker.hp)}, Moves: {[move.name for move in attacker.moveset]}")
    print(f"Defender: {defender.name}, HP: {round(defender.hp)}, Moves: {[move.name for move in defender.moveset]}")

    move = int(input(f"which move would {attacker.name} like to execute? "))

    attacker.moveset[move].execute(attacker, defender)
    print(f"{attacker.name} used {attacker.moveset[move].name} on {defender.name}\n")

    turn = 2 if turn == 1 else 1
