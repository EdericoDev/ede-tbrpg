# abilities.py

import random


def zombie_bite(player):
    print(f"The Zombie bites {player.name}!")
    player.health -= 10

def sorcerer_heal(enemy):
    heal_amount = random.randint(15, 25)
    enemy.health += heal_amount
    print(f"The Sorcerer heals itself for {heal_amount} HP!")

def demoniac_rage(player):
    print(f"The Demoniac Entity goes into a rage!")
    player.health -= random.randint(20, 30)

def goblin_sneak_attack(player):
    print(f"The Goblin performs a sneak attack!")
    player.health -= 15

def interdimensional_teleport(player):
    print(f"The Interdimensional Entity teleports away, avoiding the attack!")
    player.health = max(0, player.health - random.randint(5, 10))
