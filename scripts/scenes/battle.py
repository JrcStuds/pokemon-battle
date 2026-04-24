import pygame
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
        self.elements.append(ui.Text((0, 0), "Battle", "dodgerblue"))
        
        self.player = battle.Battler(self, pygame.Rect(0, 20, g.DISPLAY_RECT.width, 20), 0, [ battle.Pokemon(self, "Charmander") ])
        self.opponent = battle.Battler(self, pygame.Rect(0, 40, g.DISPLAY_RECT.width, 20), 1, [ battle.Pokemon(self, "Bulbasaur") ])
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

    
    def queue_move(self, move, target):
        self.queued_moves.append([move, target])


    def execute_queued_moves(self):
        self.queued_moves.sort(key=lambda move: move[0].pokemon.speed)
        for move in self.queued_moves:
            print(move[0].name)

        self.queued_moves = []
        self.menu_stack = []
        menus.GeneralBattleMenu(self).enter_state()