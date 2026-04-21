import json


class Move():
    def __init__(self, name):
        self.name = name

        with open("data/databases/moves.json", "r") as file:
            moves_db = json.load(file)

        self.type = moves_db[name]["type"]
        self.category = moves_db[name]["category"]
        self.accuracy = moves_db[name]["accuracy"]
        self.pp = moves_db[name]["pp"]
        self.power = moves_db[name]["power"]


    def execute(self, user, target):
        atk_stat = user.attack if self.category == "physical" else user.sp_attack
        def_stat = target.defense if self.category == "physical" else target.sp_defense
        target.hp -= (((2/5)+2)*self.power*(atk_stat/def_stat))/50+2