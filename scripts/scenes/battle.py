import pygame, random, json
import assets.config.globals as g
import scripts.scenes as scenes
import scripts.ui as ui
import scripts.battle as battle
import scripts.battle.menu_states as menus



class Battle(scenes.SceneBaseClass):
    def __init__(self):
        super().__init__()

        self.menu_stack = []   # menus are layered over one another, top-most is rendered
        self.queued_moves = []   # moves from the player/opponent (from their active pokemon)
        self.state = "selecting_move"   # can also be "processing_moves"

        self.background = "white"

        with open("assets/data/type_chart.json", "r") as file:   # load type chart
            self.type_chart = json.load(file)
        
        # create battlers
        self.player = battle.Battler(
            battle=self,
            rect=g.POKEMON_INFO_RECTS["player"],
            pokemon=["Charmander"]
        )
        self.opponent = battle.Battler(
            battle=self,
            rect=g.POKEMON_INFO_RECTS["opponent"],
            pokemon=["Bulbasaur"]
        )
        self.attacker = self.player
        self.defender = self.opponent

        self.add_elements(self.player, self.opponent)

        menus.GeneralBattleMenu(self).enter_state()   # start in the general menu
    

    def handle_event(self, event):
        if len(self.menu_stack):   # pass down event call to topmost menu
            self.menu_stack[-1].handle_event(event)


    def update(self, dt):
        if len(self.queued_moves) == 1:   # when the player has submitted their move, submit the opponent's
            self.defender.execute_random_move(self.attacker.active_pokemon)
            self.execute_queued_moves()

        # process tasks one at a time -> if no (not self.menu_stack), all tasks would be actioned at once
        while self.state == "processing_moves" and not self.menu_stack:
            if not self.battle_tasks:   # change state if there are no more tasks to action
                self.state = "selecting_move"
                menus.GeneralBattleMenu(self).enter_state()
                continue

            task = self.battle_tasks.pop(0)  # take the first-most task
            match task["type"]:
                case "damage":
                    task["target"].take_damage(task["damage"])
                    task["target"].battler.update_text()
                case "dialogue":
                    menus.DialogueMenu(self, task["text"]).enter_state()
                case "end_move":   # check for any dead pokemon (damage has been taken)
                    if round(self.attacker.active_pokemon.hp) <= 0:
                        g.scene_manager.change_scene(scenes.GameEnd(winner=self.opponent.active_pokemon.name))
                    if round(self.opponent.active_pokemon.hp) <= 0:
                        g.scene_manager.change_scene(scenes.GameEnd(winner=self.player.active_pokemon.name))


    def draw(self):
        blits = super().draw()   # call draw on all elements
        if self.menu_stack:   # call draw on the top-most menu
            top_menu = self.menu_stack[-1]
            if hasattr(top_menu, "draw"):
                blits.extend(top_menu.draw())
        return blits

    
    def queue_move(self, move):
        self.queued_moves.append(move)


    def execute_queued_moves(self):
        self.queued_moves.sort(key=lambda move: move["move"].pokemon.speed)
        self.menu_stack = []
        self.battle_tasks = []

        for move in self.queued_moves:
            damage = self.calculate_damage(move["move"], move["target"])
            
            # used move -> damage -> crit -> type matchup
            self.battle_tasks.append({"type": "dialogue", "text": f"{move['move'].pokemon.name} used {move['move'].name}"})
            self.battle_tasks.append({"type": "damage", "damage": damage["damage"], "target": move["target"]})
            if damage["critical"]: self.battle_tasks.append({"type": "dialogue", "text": "Critical hit!"})
            match damage["effective"]:
                case 0.5: self.battle_tasks.append({"type": "dialogue", "text": "It's not very effective..."})
                case 2: self.battle_tasks.append({"type": "dialogue", "text": "It's super effective!"})
            self.battle_tasks.append({"type": "end_move"})
        
        self.queued_moves = []
        self.state = "processing_moves"


    def calculate_damage(self, move, target):
        # select physical/special stats to use
        atk_stat = move.pokemon.attack if move.type == "physical" else move.pokemon.sp_attack
        def_stat = target.defense if move.type == "physical" else target.sp_defense

        critical = random.randint(0, 15) // 15 + 1   # 1/16 chance -> 1 or 2
        type_mult = self.type_chart[move.type][target.type]   # chart goes [attacking type][defending type]
        stab = 1.5 if move.type == move.pokemon.type else 1
        random_mult = random.randint(85, 100) / 100   # uniform random variation (85-100% strength)

        # damage formula
        damage = 2 * move.pokemon.level / 5 + 2
        damage *= move.power * atk_stat / def_stat / 50 + 2
        damage *= critical * type_mult * stab * random_mult

        return {
            "damage": damage,
            "critical": bool(critical - 1),
            "effective": type_mult
        }