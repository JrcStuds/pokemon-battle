import json
import scripts.battle.menu_states as menus
from .move import Move


class Pokemon():
    def __init__(self, battler, args):
        self.name = args[0]
        self.battler = battler

        with open("assets/data/pokemon.json", "r") as file:
            pokemon_db = json.load(file)
        
        self.lv = args[1] if len(args) > 1 else 49
        self.type = pokemon_db[self.name]["type"]
        self.max_hp = round(self.modify_stat_hp(pokemon_db[self.name]["hp"], self.lv))
        self.hp = self.max_hp
        self.attack = self.modify_stat(pokemon_db[self.name]["attack"], self.lv)
        self.defense = self.modify_stat(pokemon_db[self.name]["defense"], self.lv)
        self.sp_attack = self.modify_stat(pokemon_db[self.name]["sp_attack"], self.lv)
        self.sp_defense = self.modify_stat(pokemon_db[self.name]["sp_defense"], self.lv)
        self.speed = self.modify_stat(pokemon_db[self.name]["speed"], self.lv)
        self.moveset = [Move(self, move) for move in pokemon_db[self.name]["moveset"]]


    # modifies hp stat based of provided damage
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0.5 and self.hp != 0:
            self.hp = 0
        return
    

    # when called, similar to a move, queues a type=switch object to the battle class to be executed
    def switch(self):
        if self.hp == 0:
            menus.DialogueMenu(self.battler.battle, "No HP left!").enter_state()
            return
        
        self.battler.battle.queue_move({
            "type": "switch",
            "battler": self.battler,
            "pokemon_idx": self.battler.pokemon.index(self)
        })


    def modify_stat(self, base, lv):
        new = (((2 * base) + 31) * lv / 100) + 5
        return new
    
    def modify_stat_hp(self, base, lv):
        new = (((2 * base) + 31) * lv / 100) + lv + 10
        return new


