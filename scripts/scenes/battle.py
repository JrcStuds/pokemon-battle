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

        self.background = "white"

        with open("assets/data/type_chart.json", "r") as file:
            self.type_chart = json.load(file)
        
        self.player = battle.Battler(self, pygame.Rect(30, 10, 80, 30), [ battle.Pokemon(self, "Charmander") ])
        self.opponent = battle.Battler(self, pygame.Rect(130, 60, 80, 30), [ battle.Pokemon(self, "Bulbasaur") ])
        self.attacker = self.opponent
        self.defender = self.player

        self.add_elements(self.player, self.opponent)

        menus.GeneralBattleMenu(battle=self).enter_state()
    

    def handle_event(self, event):
        if len(self.menu_stack):
            self.menu_stack[-1].handle_event(event)


    def update(self, dt):
        if len(self.queued_moves) == 1:
            self.defender.execute_random_move(self.attacker.active_pokemon)
        if len(self.queued_moves) == 2:
            self.execute_queued_moves()

    
    def queue_move(self, move):
        self.queued_moves.append(move)


    def execute_queued_moves(self):
        self.queued_moves.sort(key=lambda move: move["move"].pokemon.speed)

        for move in self.queued_moves:
            damage = self.calculate_damage(move["move"], move["target"])
            print(f"{move['move'].pokemon.name} used {move['move'].name} on {move['target'].name}")
            print(f"{move['target'].name}'s HP went from {round(move['target'].hp)}")
            move["target"].take_damage(damage)
            print(f"to {round(move['target'].hp)}")

        self.player.update_text()
        self.opponent.update_text()

        self.queued_moves = []
        self.menu_stack = []
        menus.GeneralBattleMenu(self).enter_state()


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

        return damage