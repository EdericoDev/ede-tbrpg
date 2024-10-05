## 🧠 **README.md**

# 🕹️ Turn-Based RPG Game

Welcome to the Turn-Based RPG Game! Battle against various enemies, choose your class, and progress through increasing levels of difficulty. Choose between **Endless Mode** or a 20-enemy challenge and prove your strength in this interactive terminal-based RPG!

## 📖 **Table of Contents**
- [Features](#features)
- [Installation](#installation)
- [Running the Game](#running-the-game)
- [Gameplay Tutorial](#gameplay-tutorial)
- [Updating the Game](#updating-the-game)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

---

## 🌟 **Features**
- **Classes:** Choose from multiple unique character classes like Cowboy, Mage, Warrior, and more.
- **Enemies:** Fight against a variety of enemies with special abilities.
- **Endless Mode:** Battle an infinite number of enemies or aim for victory by defeating 20 enemies.
- **Increasing Difficulty:** Enemies get harder with each encounter based on your chosen difficulty level.
- **Leveling System:** Gain experience, level up, and grow stronger after defeating enemies.

---

## 🚀 **Installation**

Follow these steps to install and set up the game on your machine.

### **Prerequisites**
1. **Python** (version 3.8 or above)
    - Ensure Python is installed on your machine. You can download it from the official [Python website](https://www.python.org/downloads/).

2. **pip** (Python's package manager)
    - `pip` is typically included with Python installations. Verify it by running:
      ```bash
      pip --version
      ```

### **1. Clone the Repository**
First, clone the game repository from GitHub (replace the link with the actual one if hosted):
```bash
git clone https://github.com/yourusername/rpg-game.git
```

### **2. Navigate to the Project Folder**
```bash
cd rpg-game
```

### **3. (Optional) Create a Virtual Environment**
Create a virtual environment to keep dependencies isolated:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **4. Install Dependencies**
```bash
pip install -r requirements.txt
```
> **Note:** The game doesn't have any external dependencies, so you can skip this step if the `requirements.txt` is empty.

---

## 🕹️ **Running the Game**

To start the game, run the following command in your terminal:

```bash
python main.py
```

You'll be prompted to select a character class, choose a difficulty level, and whether or not to activate **Endless Mode**. Then, let the adventure begin!

---

## 🎮 **Gameplay Tutorial**

### **1. Character Selection**
At the start of the game, you'll be asked to select your character class:
```plaintext
[1] Cowboy - Hunting Rifle
[2] Mage - Mystic Book
[3] Warrior - Sword
[4] Potato - Grass Bombs
[5] Commando - Suppressor Pistol
[6] Mutant - Spore Bombs
```
Choose a class by entering the corresponding number (1–6).

### **2. Difficulty Selection**
Select your difficulty:
```plaintext
[1] Easy
[2] Medium
[3] Hard
[4] Extreme
```

### **3. Endless Mode**
You will be asked if you want to activate **Endless Mode**:
```plaintext
Do you want to activate Endless Mode? [y/n]:
```
- **Yes (y):** The game will go on indefinitely with increasing difficulty.
- **No (n):** The game ends after defeating 20 enemies.

### **4. Battle Phases**
Each turn, you can choose to attack normally or use a special attack:
```plaintext
Choose an action: [1] Normal Attack [2] Special Attack
```
- **Normal Attack:** Deals regular damage.
- **Special Attack:** Uses mana and executes your class-specific move.

### **5. Leveling Up**
- Gain XP after defeating enemies.
- Once you gain enough XP, you will level up, increasing your health and attack power.

---

## 🔄 **Updating the Game**

To pull the latest changes from the repository, navigate to your game directory and run:
```bash
git pull origin main
```

If there are new dependencies added, install them:
```bash
pip install -r requirements.txt
```

---

## 🛠️ **Troubleshooting**

### **Common Issues:**
- **Game doesn't start:**
    - Ensure Python is installed correctly and that you’re using Python 3.8 or higher.
    - Ensure you're in the correct directory (`cd rpg-game`).
  
- **Missing `pip`:**
    - Reinstall Python with `pip` included or install `pip` manually by following [this guide](https://pip.pypa.io/en/stable/installation/).

- **Game crashes during enemy attack:**
    - Ensure your Python environment is clean. Try deleting the `venv` folder and recreating it with:
      ```bash
      python -m venv venv
      ```

---

## 🤝 **Contributing**

We welcome contributions! Feel free to fork the project and submit a pull request. Here's how to contribute:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-branch-name
    ```
3. Commit your changes:
    ```bash
    git commit -m "Description of changes"
    ```
4. Push to your branch:
    ```bash
    git push origin feature-branch-name
    ```
5. Create a pull request on GitHub!

---

## 📜 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

---
