import pygame
import assets.config.globals as g
import scripts.ui as ui
import scripts.battle.menu_states as menus
from .menu_base_scene import BattleMenuSceneBaseClass



class PokemonBattleMenu(BattleMenuSceneBaseClass):
    def __init__(self, battle, mandatory: bool = False):
        super().__init__(battle=battle, background=ui.image.create_surface_from_spritesheet("menus", "pokemon_bg"))

        self.mandatory = mandatory   # used for if current pokemon has just fainted and not allowed to go back
        self.buttons = []
        
        # add the active pokemon's ui elements
        self.buttons.append(ui.ImageButton(
            callback=lambda: menus.DialogueMenu(battle=self.battle, text="Nothing happened...").enter_state(),
            pos=g.BATTLE_MENU_RECTS["pokemon"][0]["container"],
            selected=True,
            image_selected=ui.image.create_surface_from_spritesheet("menus", "pokemon_active_selected"),
            image_unselected=ui.image.create_surface_from_spritesheet("menus", "pokemon_active")
        ))
        self.add_elements(
            self.buttons[-1],
            ui.Image(
                pos=g.BATTLE_MENU_RECTS["pokemon"][0]["image"],
                spritesheet="pokemon",
                name=self.battle.attacker.active_pokemon.name,
                type="mini"
            ),
            ui.Text(
                pos=g.BATTLE_MENU_RECTS["pokemon"][0]["name"],
                text=self.battle.attacker.active_pokemon.name.title(),
                type="small",
                col="light"
            ),
            ui.HpBar(
                pos=g.BATTLE_MENU_RECTS["pokemon"][0]["hp_bar"],
                value=round(self.battle.attacker.active_pokemon.hp / self.battle.attacker.active_pokemon.max_hp * 48)
            ),
            ui.Text(
                pos=g.BATTLE_MENU_RECTS["pokemon"][0]["hp_text"],
                text=f"{round(self.battle.attacker.active_pokemon.hp)}/{self.battle.attacker.active_pokemon.max_hp}",
                type="small",
                col="light",
                alignment="right"
            ),
            ui.Text(
                pos=g.BATTLE_MENU_RECTS["pokemon"]["title"],
                text="Choose a Pokemon."
            )
        )
        
        # loop through the pokemon in the attacker's pokemon list and add ui elements for all non-active pokemon
        j = 1
        for i in range(len(self.battle.attacker.pokemon)):
            if len(self.battle.attacker.pokemon) <= j:
                break
            if self.battle.attacker.pokemon[i] == self.battle.attacker.active_pokemon:
                continue

            self.buttons.append(ui.ImageButton(
                callback=lambda i=i: self.battle.attacker.pokemon[i].switch(),
                pos=g.BATTLE_MENU_RECTS["pokemon"][j]["container"],
                selected=False,
                image_selected=ui.image.create_surface_from_spritesheet("menus", "pokemon_long_selected"),
                image_unselected=ui.image.create_surface_from_spritesheet("menus", "pokemon_long")
            ))
            
            self.add_elements(
                self.buttons[-1],
                ui.Image(
                    pos=g.BATTLE_MENU_RECTS["pokemon"][j]["image"],
                    spritesheet="pokemon",
                    name=self.battle.attacker.pokemon[i].name,
                    type="mini"
                ),
                ui.Text(
                    pos=g.BATTLE_MENU_RECTS["pokemon"][j]["name"],
                    text=self.battle.attacker.pokemon[i].name.title(),
                    type="small",
                    col="light"
                ),
                ui.HpBar(
                    pos=g.BATTLE_MENU_RECTS["pokemon"][j]["hp_bar"],
                    value=round(self.battle.attacker.pokemon[i].hp / self.battle.attacker.pokemon[i].max_hp * 48)
                ),
                ui.Text(
                    pos=g.BATTLE_MENU_RECTS["pokemon"][j]["hp_text"],
                    text=f"{round(self.battle.attacker.pokemon[i].hp)}/{self.battle.attacker.pokemon[i].max_hp}",
                    type="small",
                    col="light",
                    alignment="right"
                )
            )

            j += 1

        self.cursor = ui.Cursor(
            buttons=self.buttons,
            type="pokemon_menu",
            visible=False
        )
        self.elements.append(self.cursor)
    

    def handle_event(self, event):
        super().handle_event(event)

        if g.keys["b"]:
            if self.mandatory:
                menus.DialogueMenu(self.battle, "You need to choose a Pokemon.").enter_state()
            else:
                self.exit_state()

    
    def update(self, dt):
        return super().update(dt)