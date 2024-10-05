# player.py
from character import Character
import random

class Player(Character):
    def __init__(self, name, character_class, health, attack_power, mana):
        super().__init__(name, health, attack_power)
        self.character_class = character_class
        self.mana = mana
        self.max_mana = mana
        self.xp = 0
        self.level = 1
        self.special_attacks = {
            'Cowboy': self.hunting_rifle,
            'Mage': self.mystic_book,
            'Warrior': self.sword,
            'Potato': self.grass_bomb,
            'Commando': self.suppressor_pistol,
            'Mutant': self.spore_bombs
        }

    def normal_attack(self, opponent):
        self.attack(opponent)

    # Special attacks with mana costs
    def hunting_rifle(self, opponent):
        if self.mana >= 10:
            self.mana -= 10
            if random.random() < 0.25:
                print(f"{self.name} missed with the hunting rifle!")
            else:
                self.attack(opponent)
        else:
            print(f"Not enough mana to use the hunting rifle!")

    def mystic_book(self, opponent):
        if self.mana >= 15:
            self.mana -= 15
            damage = random.randint(self.attack_power + 5, self.attack_power + 15)
            opponent.health -= damage
            print(f"{self.name} casts a spell from the Mystic Book for {damage} damage!")
        else:
            print(f"Not enough mana to use the Mystic Book!")

    def sword(self, opponent):
        if self.mana >= 5:
            self.mana -= 5
            self.attack(opponent)
        else:
            print(f"Not enough mana to use the Sword!")

    def grass_bomb(self, opponent):
        if self.mana >= 12:
            self.mana -= 12
            damage = random.randint(self.attack_power + 10, self.attack_power + 20)
            opponent.health -= damage
            print(f"{self.name} throws a grass bomb for {damage} damage!")
        else:
            print(f"Not enough mana to use the Grass Bomb!")

    def suppressor_pistol(self, opponent):
        if self.mana >= 8:
            self.mana -= 8
            self.attack(opponent)
            if random.random() < 0.2:
                print(f"{opponent.name} is put to sleep and will miss their next turn!")
        else:
            print(f"Not enough mana to use the Suppressor Pistol!")

    def spore_bombs(self, opponent):
        if self.mana >= 18:
            self.mana -= 18
            damage = random.randint(self.attack_power + 15, self.attack_power + 25)
            opponent.health -= damage
            print(f"{self.name} throws spore bombs for {damage} damage!")
        else:
            print(f"Not enough mana to use the Spore Bombs!")

    def gain_xp(self, xp, difficulty):
        self.xp += xp
        print(f"{self.name} gains {xp} XP!")
        if self.xp >= self.level * 100:
            self.level_up(difficulty)

    def level_up(self, difficulty):
        self.level += 1
        self.xp = 0
        self.health += 20
        self.attack_power += 5
        print(f"{self.name} leveled up to level {self.level}! Health and Attack Power increased!")

        # Chance to restore mana on level up
        restore_chance = {
            "Easy": 0.4,
            "Medium": 0.3,
            "Hard": 0.2,
            "Extreme": 0.1
        }
        if random.random() < restore_chance[difficulty]:
            if random.random() < 0.2:  # 20% chance to fully restore mana
                self.mana = self.max_mana
                print(f"Full mana restored on level up!")
            else:  # 30% chance to restore half of the mana
                mana_restored = self.max_mana // 2
                self.mana += mana_restored
                print(f"Partial mana restored: {mana_restored} mana!")
