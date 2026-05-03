import pygame
import assets.config.globals as g
import scripts.ui as ui
import scripts.battle.menu_states as menus
from .menu_base_scene import BattleMenuSceneBaseClass



class PokemonBattleMenu(BattleMenuSceneBaseClass):
    def __init__(self, battle):
        super().__init__(battle=battle, background=ui.image.create_surface_from_spritesheet("menus", "pokemon_bg"))

        self.buttons = []

        self.buttons.append(ui.ImageButton(
            callback=lambda: menus.DialogueMenu(battle=self.battle, text="Nothing happened..."),
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
                text=self.battle.attacker.active_pokemon.name,
                type="small",
                col="light"
            )
        )

        j = 1
        for i in range(len(self.battle.attacker.pokemon)):
            if len(self.battle.attacker.pokemon) <= j:
                break
            if self.battle.attacker.pokemon[i] == self.battle.attacker.active_pokemon:
                continue

            self.buttons.append(ui.ImageButton(
                callback=lambda i=i: self.battle.queue_move({
                    "type": "switch",
                    "battler": self.battle.attacker,
                    "pokemon_idx": i
                }),
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
                    text=self.battle.attacker.pokemon[i].name,
                    type="small",
                    col="light"
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
            self.exit_state()

    
    def update(self, dt):
        return super().update(dt)