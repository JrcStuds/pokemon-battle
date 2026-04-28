import pygame, random, json
import assets.config.globals as g
import scripts.scenes as scenes
import scripts.ui as ui
import scripts.battle as battle
import scripts.battle.menu_states as menus



class Battle(scenes.SceneBaseClass):
    def __init__(self):
        super().__init__()

        self.menu_stack = []
        self.queued_moves = []
        self.state = "selecting_move"   # can also be "processing_moves"

        self.background = "white"

        with open("assets/data/type_chart.json", "r") as file:
            self.type_chart = json.load(file)
        
        self.player = battle.Battler(
            battle=self,
            rect=g.POKEMON_INFO_RECTS["player"],
            pokemon=[ battle.Pokemon(self, "Charmander") ]
        )
        self.opponent = battle.Battler(
            battle=self,
            rect=g.POKEMON_INFO_RECTS["opponent"],
            pokemon=[ battle.Pokemon(self, "Bulbasaur") ]
        )
        self.attacker = self.player
        self.defender = self.opponent

        self.add_elements(self.player, self.opponent)

        menus.GeneralBattleMenu(self).enter_state()
    

    def handle_event(self, event):
        if len(self.menu_stack):
            self.menu_stack[-1].handle_event(event)


    def update(self, dt):
        if len(self.queued_moves) == 1:
            self.defender.execute_random_move(self.attacker.active_pokemon)
            self.execute_queued_moves()

        if self.state == "processing_moves" and not self.menu_stack:
            if self.battle_tasks:
                task = self.battle_tasks.pop(0)

                if task["type"] == "dialogue":
                    for dialogue in task["dialogues"]:
                        menus.DialogueMenu(self, dialogue).enter_state()
                
                elif task["type"] == "damage":
                    task["target"].take_damage(task["damage"])
                    self.player.update_text()
                    self.opponent.update_text()
            
            else:
                self.state = "selecting_move"
                menus.GeneralBattleMenu(self).enter_state()

        if round(self.attacker.active_pokemon.hp) <= 0:
            g.scene_manager.change_scene(scenes.GameEnd(winner=self.opponent.active_pokemon.name))
        if round(self.opponent.active_pokemon.hp) <= 0:
            g.scene_manager.change_scene(scenes.GameEnd(winner=self.player.active_pokemon.name))

    
    def queue_move(self, move):
        self.queued_moves.append(move)


    def execute_queued_moves(self):
        self.queued_moves.sort(key=lambda move: move["move"].pokemon.speed)

        self.menu_stack = []
        self.battle_tasks = []

        for move in self.queued_moves:
            damage = self.calculate_damage(move["move"], move["target"])

            dialogues = []
            match damage["effective"]:
                case 0.5: dialogues.append("It's not very effective...")
                case 2: dialogues.append("It's super effective!")
            if damage["critical"]: dialogues.append("Critical hit!")
            dialogues.append(f"{move['move'].pokemon.name} used {move['move'].name}")

            self.battle_tasks.append({"type": "damage", "damage": damage["damage"], "target": move["target"]})
            self.battle_tasks.append({"type": "dialogue", "dialogues": dialogues})
        
        self.queued_moves = []
        self.state = "processing_moves"


    def calculate_damage(self, move, target):
        atk_stat = move.pokemon.attack if move.type == "physical" else move.pokemon.sp_attack
        def_stat = target.defense if move.type == "physical" else target.sp_defense

        critical = random.randint(0, 15) // 15 + 1   # 1/16 chance -> 1 or 2
        type_mult = self.type_chart[move.type][target.type]   # chart goes [attacking type][defending type]
        stab = 1.5 if move.type == move.pokemon.type else 1
        random_mult = random.randint(85, 100) / 100   # uniform random variation (85-100% strength)

        damage = 2 * move.pokemon.level / 5 + 2
        damage *= move.power * atk_stat / def_stat / 50 + 2
        damage *= critical * type_mult * stab * random_mult

        return {
            "damage": damage,
            "critical": bool(critical - 1),
            "effective": type_mult
        }