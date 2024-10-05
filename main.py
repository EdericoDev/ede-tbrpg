from player import Player
from enemy import generate_enemy
from utilities import display_stats, set_difficulty

def game():
    print("Welcome to the game!")

    # Name and character selection
    player_name = input("Enter your character's name: ")
    print("\nSelect your class:")
    print("[1] Cowboy - Hunting Rifle")
    print("[2] Mage - Mystic Book")
    print("[3] Warrior - Sword")
    print("[4] Potato - Grass Bombs")
    print("[5] Commando - Suppressor Pistol")
    print("[6] Mutant - Spore Bombs")
    
    class_choice = input("Choose your class: ")
    class_map = {
        '1': 'Cowboy', '2': 'Mage', '3': 'Warrior',
        '4': 'Potato', '5': 'Commando', '6': 'Mutant'
    }
    player_class = class_map.get(class_choice, 'Warrior')  # Default to Warrior if invalid choice

    # Difficulty selection
    print("\nSelect difficulty:")
    print("[1] Easy")
    print("[2] Medium")
    print("[3] Hard")
    print("[4] Extreme")

    difficulty_choice = input("Choose difficulty: ")
    difficulty_map = {
        '1': "Easy", '2': "Medium", '3': "Hard", '4': "Extreme"
    }
    difficulty = difficulty_map.get(difficulty_choice, "Medium")

    # New: Endless mode or 20th enemy cap
    endless_mode = input("Do you want to activate Endless Mode? [y/n]: ").lower() == "y"
    enemy_limit = 20  # Max number of enemies if Endless Mode is off
    enemy_count = 0  # Track number of defeated enemies

    # Initialize player with chosen class and difficulty settings
    health, attack_power = set_difficulty(difficulty)
    player = Player(player_name, player_class, health, attack_power, mana=50)

    # Main game loop
    while player.is_alive():
        enemy = generate_enemy(player_class)
        enemy_count += 1
        print(f"\nA wild {enemy.name} appears! (Enemy #{enemy_count})")

        while enemy.is_alive() and player.is_alive():
            display_stats(player, enemy)

            # Player's turn
            print("Your turn!")
            action = input("Choose an action: [1] Normal Attack [2] Special Attack: ")

            if action == "1":
                player.normal_attack(enemy)
            elif action == "2":
                player.special_attacks[player.character_class](enemy)
            else:
                print("Invalid action! You miss your turn.")

            # Check if enemy is defeated
            if not enemy.is_alive():
                print(f"{enemy.name} is defeated!")
                player.gain_xp(enemy.xp_reward, difficulty)
                break

            # Enemy's turn
            print("Enemy's turn!")
            if enemy.special_move:
                enemy.use_special_move(player)
            else:
                enemy.attack(player)

            if not player.is_alive():
                print(f"{player.name} has been defeated. Game over!")
                return  # Exit the game loop

        # Check if player has reached the limit and isn't in Endless Mode
        if not endless_mode and enemy_count >= enemy_limit:
            print(f"\nYou've defeated 20 enemies and won the game!")
            return  # End game after 20th enemy

    print("Game Over!")

# Start the game
if __name__ == "__main__":
    game()
