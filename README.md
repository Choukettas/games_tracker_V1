# 🎮 Giveaway Bot Discord

This project is a **Python bot** that monitors multiple video game platforms and automatically sends **new giveaways** to Discord via webhooks.

It supports the following platforms:  
- Steam (games and DLC)  
- Epic Games Store (games and DLC)  
- GOG  
- PlayStation  
- Xbox  
- Nintendo Switch  

The bot regularly checks for new giveaways and only sends those that have not been posted yet.

---

## 🚀 Features

- Automatically checks for new giveaways every **5 minutes**.  
- Sends notifications to Discord via **customizable webhooks**.  
- Handles errors and invalid data so the bot continues running even if one platform fails.  
- Supports **games and DLC** separately.  
- Multi-platform support: Steam, Epic Games, GOG, PlayStation, Xbox, Switch.

---

## 🔧 Project Structure

free_games_tracker/
│
├─ main.py # Main script
├─ data/ # Giveaway JSON files
│ ├─ steam_game.json
│ ├─ epicgame_game.json
│ ├─ steam_DLC.json
│ ├─ epicgame_DLC.json
│ ├─ gog_game.json
│ ├─ playstation.json
│ ├─ xbox.json
│ └─ switch.json
├─ requirements.txt # Python dependencies
└─ README.md # Project documentation

---

## ⚙️ Installation

1. **Clone the repository**:  
```bash
git clone https://github.com/Choukettas/free_games_tracker.git
cd free_games_tracker
