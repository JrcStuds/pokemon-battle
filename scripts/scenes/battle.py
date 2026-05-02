import pygame, random, json
import assets.config.globals as g
import scripts.scenes as scenes
import scripts.ui as ui
import scripts.battle as battle
import scripts.battle.menu_states as menus



class Battle(scenes.SceneBaseClass):
    def __init__(self, background = "white"):
        super().__init__(background=pygame.image.load("assets/images/backgrounds.png").convert_alpha().subsurface(g.BACKGROUND_SPRITESHEET_RECT))

        self.menu_stack = []   # menus are layered over one another, top-most is rendered
        self.queued_moves = []   # moves from the player/opponent (from their active pokemon)
        self.state = "selecting_move"   # can also be "processing_moves"

        with open("assets/data/type_chart.json", "r") as file:   # load type chart
            self.type_chart = json.load(file)
        
        # create battlers
        self.player = battle.Battler(
            battle=self,
            pokemon=["Charmander", "Bulbasaur", "Charmander"],
            attacker=True
        )
        self.opponent = battle.Battler(
            battle=self,
            pokemon=["Bulbasaur"],
            attacker=False
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
            self.defender.execute_random_move(target=self.attacker)
            self.execute_queued_moves()

        # process tasks one at a time -> if no (not self.menu_stack), all tasks would be actioned at once
        while self.state == "processing_moves" and not self.menu_stack:
            if not self.battle_tasks:   # change state if there are no more tasks to action
                self.state = "selecting_move"
                menus.GeneralBattleMenu(self).enter_state()
                continue

            task = self.battle_tasks.pop(0)  # take the first-most task
            self.process_task(task)
        
        for menu in self.menu_stack:
            if hasattr(menu, "update"):
                menu.update(dt)


    def draw(self):
        blits = super().draw()   # call draw on all elements
        for menu in self.menu_stack:
            if hasattr(menu, "draw"):
                blits.extend(menu.draw())
        return blits

    
    def queue_move(self, move):
        self.queued_moves.append(move)


    def sort_queued_moves(self, queued_moves: list) -> list:
        switches, moves = [], []
        for move in queued_moves:
            if move["type"] == "move":
                moves.append(move)
            elif move["type"] == "switch":
                switches.append(move)
        moves.sort(key=lambda move: move["move"].pokemon.speed)
        queued_moves = switches
        queued_moves.extend(moves)
        return queued_moves


    def execute_queued_moves(self):
        self.queued_moves = self.sort_queued_moves(self.queued_moves)
        self.menu_stack = []
        self.battle_tasks = []

        for move in self.queued_moves:
            if move["type"] == "move":
                damage = self.calculate_damage(move["move"], move["target"].active_pokemon)
                
                # used move -> damage -> crit -> type matchup
                self.battle_tasks.append({"type": "dialogue", "text": f"{move['move'].pokemon.name} used {move['move'].name}", "foe": move["move"].pokemon.battler==self.opponent})
                self.battle_tasks.append({"type": "damage", "damage": damage["damage"], "target": move["target"]})
                if damage["critical"]: self.battle_tasks.append({"type": "dialogue", "text": "Critical hit!"})
                match damage["effective"]:
                    case 0.5: self.battle_tasks.append({"type": "dialogue", "text": "It's not very effective..."})
                    case 2: self.battle_tasks.append({"type": "dialogue", "text": "It's super effective!"})
            
            elif move["type"] == "switch":
                self.battle_tasks.append({"type": "dialogue", "text": f"Come back, {move['battler'].active_pokemon.name}!"})
                self.battle_tasks.append({"type": "switch", "battler": move["battler"], "pokemon_idx": move["pokemon_idx"]})
                self.battle_tasks.append({"type": "dialogue", "text": f"Let's go, {move['battler'].pokemon[move['pokemon_idx']].name}!"})
                
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


    def process_task(self, task):
        match task["type"]:
            case "damage":
                task["target"].active_pokemon.take_damage(task["damage"])
                task["target"].update_text()
            case "dialogue":
                text = task["text"]
                if "foe" in task.keys():
                    if task["foe"]: text = "Foe " + text
                menus.DialogueMenu(self, text).enter_state()
            case "end_move":   # check for any dead pokemon (damage has been taken)
                if round(self.attacker.active_pokemon.hp) <= 0:
                    g.scene_manager.change_scene(scenes.GameEnd(winner=self.opponent.active_pokemon.name))
                if round(self.opponent.active_pokemon.hp) <= 0:
                    g.scene_manager.change_scene(scenes.GameEnd(winner=self.player.active_pokemon.name))
            case "switch":
                task["battler"].active_pokemon = task["battler"].pokemon[task["pokemon_idx"]]
                task["battler"].update_text()