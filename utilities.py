def display_stats(player, enemy):
    print(f"\n{player.name} (Level {player.level}): {player.health} HP | Mana: {player.mana}/{player.max_mana}")
    print(f"{enemy.name}: {enemy.health} HP\n")

def set_difficulty(difficulty):
    if difficulty == "Easy":
        return 50, 12  
    elif difficulty == "Medium":
        return 70, 17  
    elif difficulty == "Hard":
        return 100, 22  
    elif difficulty == "Extreme":
        return 150, 30  
    else:
        print("Invalid difficulty. Defaulting to Medium.")
        return 70, 17

