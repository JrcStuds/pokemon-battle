from scripts.battle.pokemon import Pokemon
from scripts.battle.battler import Battler


class Battle():
    def __init__(self):
        self.player_one = Battler([ Pokemon("Charmander") ])
        self.player_two = Battler([ Pokemon("Bulbasaur") ])