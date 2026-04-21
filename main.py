from scripts.battle import Battle



battle = Battle()

turn = 1
running = True
while running:
    attacker = battle.player_one.pokemon[0] if turn == 1 else battle.player_two.pokemon[0]
    defender = battle.player_one.pokemon[0] if turn == 2 else battle.player_two.pokemon[0]


    if round(attacker.hp) <= 0:
        print(f"{defender.name} Wins!")
        running = False
        continue


    print(f"Attacker: {attacker.name}, HP: {round(attacker.hp)}, Moves: {[move.name for move in attacker.moveset]}")
    print(f"Defender: {defender.name}, HP: {round(defender.hp)}, Moves: {[move.name for move in defender.moveset]}")

    move = int(input(f"which move would {attacker.name} like to execute? "))

    attacker.moveset[move].execute(attacker, defender)
    print(f"{attacker.name} used {attacker.moveset[move].name} on {defender.name}\n")

    turn = 2 if turn == 1 else 1
