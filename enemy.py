from abilities import demoniac_rage, goblin_sneak_attack, interdimensional_teleport, sorcerer_heal, zombie_bite
from character import Character
import random

class Enemy(Character):
    def __init__(self, name, health, attack_power, xp_reward, special_move=None):
        super().__init__(name, health, attack_power)
        self.xp_reward = xp_reward
        self.special_move = special_move

    def use_special_move(self, player):
        if self.special_move:
            self.special_move(player)

# Enemy generator with harder enemies
def generate_enemy(player_class):
    enemy_types = [
        ("Zombie", zombie_bite),
        ("Sorcerer", sorcerer_heal),
        ("Demoniac Entity", demoniac_rage),
        ("Goblin", goblin_sneak_attack),
        ("Interdimensional Entity", interdimensional_teleport),
    ]

    # 1% chance for a Virtual Avatar (same class as player)
    if random.random() < 0.01:
        return Enemy(f"Virtual Avatar {player_class}", 120, 25, xp_reward=200, special_move=None)

    enemy_name, special_move = random.choice(enemy_types)
    return Enemy(enemy_name, random.randint(60, 120), random.randint(15, 30), xp_reward=150, special_move=special_move)

