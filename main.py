import requests
import json
import time
from datetime import datetime
import os

url = "https://www.gamerpower.com/api/giveaways"
webhook_url_game = "Your token webhook"
webhook_url_DLC = "Your token webhook"
ping_target = "Role of ping"

params_steam_game = {
    "platform": "steam",
    "type": "game"
}

params_epicgame_game = {
    "platform": "epic-games-store",
    "type": "game"
}

params_steam_DLC = {
    "platform": "steam",
    "type": "loot"
}

params_epicgame_DLC = {
    "platform": "epic-games-store",
    "type": "loot"
}

print("Bot lancé...")

while True:
    try:

        old_id = None
        if os.path.exists("./data/steam_game.json"):
            with open("./data/steam_game.json", "r", encoding="utf-8") as f:
                old_data = json.load(f)
                if isinstance(old_data, list) and old_data:
                    old_id = old_data[0].get("id")

        
        r = requests.get(url, params=params_steam_game, timeout=5)
        r.raise_for_status()
        data = r.json()

        if not data or not isinstance(data, list):
            print("⚠️ Données invalides")
            time.sleep(5)
            continue

        d = data[0]
        current_id = d.get("id")


        if old_id == current_id:
            print("⏩ Déjà envoyé, on ignore")

        else:
            print("🆕 Nouveau jeu détecté")

            payload = {
                "content": ping_target,
                "embeds": [
                    {
                        "thumbnail": { "url": "https://i.postimg.cc/hjrPkWbj/S2Qw-Qtm.png" },
                        "title": d.get("title"),
                        "description": (
                            f"{d.get('description')}\n\n"
                            f"~~{d.get('worth')}~~ **Gratuit jusqu’au {d.get('end_date')}**\n"
                            f"🔗 [Ouvrir dans la boutique]({d.get('open_giveaway')})"
                        ),
                        "color": 0x7F00FF,
                        "footer": { "text": "by choukettas" },
                        "timestamp": datetime.utcnow().isoformat(),
                        "image": { "url": d.get("image") }
                    }
                ]
            }

            requests.post(webhook_url_game, json=payload)
            print(f"[OK] {d.get('title')} envoyé")

            with open("./data/steam_game.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

    except Exception as e:
        print("Erreur :", e)

    try:

        old_id = None
        if os.path.exists("./data/epicgame_game.json"):
            with open("./data/epicgame_game.json", "r", encoding="utf-8") as f:
                old_data = json.load(f)
                if isinstance(old_data, list) and old_data:
                    old_id = old_data[0].get("id")

        
        r = requests.get(url, params=params_epicgame_game, timeout=5)
        r.raise_for_status()
        data = r.json()

        if not data or not isinstance(data, list):
            print("⚠️ Données invalides")
            time.sleep(5)
            continue

        d = data[0]
        current_id = d.get("id")


        if old_id == current_id:
            print("⏩ Déjà envoyé, on ignore")

        else:
            print("🆕 Nouveau jeu détecté")

            payload = {
                "content": ping_target,
                "embeds": [
                    {
                        "thumbnail": { "url": "https://i.postimg.cc/k4cX03F5/6Zjdyt-V.png" },
                        "title": d.get("title"),
                        "description": (
                            f"{d.get('description')}\n\n"
                            f"~~{d.get('worth')}~~ **Gratuit jusqu’au {d.get('end_date')}**\n"
                            f"🔗 [Ouvrir dans la boutique]({d.get('open_giveaway')})"
                        ),
                        "color": 0x7F00FF,
                        "footer": { "text": "by choukettas" },
                        "timestamp": datetime.utcnow().isoformat(),
                        "image": { "url": d.get("image") }
                    }
                ]
            }

            requests.post(webhook_url_game, json=payload)
            print(f"[OK] {d.get('title')} envoyé")

            with open("./data/epicgame_game.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

    except Exception as e:
        print("Erreur :", e)  

    try:

        old_id = None
        if os.path.exists("./data/epicgame_DLC.json"):
            with open("./data/epicgame_DLC.json", "r", encoding="utf-8") as f:
                old_data = json.load(f)
                if isinstance(old_data, list) and old_data:
                    old_id = old_data[0].get("id")

        
        r = requests.get(url, params=params_epicgame_DLC, timeout=5)
        r.raise_for_status()
        data = r.json()

        if not data or not isinstance(data, list):
            print("⚠️ Données invalides")
            time.sleep(5)
            continue

        d = data[0]
        current_id = d.get("id")


        if old_id == current_id:
            print("⏩ Déjà envoyé, on ignore")

        else:
            print("🆕 Nouveau DCL détecté")

            payload = {
                "content": ping_target,
                "embeds": [
                    {
                        "thumbnail": { "url": "https://i.postimg.cc/k4cX03F5/6Zjdyt-V.png" },
                        "title": d.get("title"),
                        "description": (
                            f"{d.get('description')}\n\n"
                            f"~~{d.get('worth')}~~ **DLC jusqu’au {d.get('end_date')}**\n"
                            f"🔗 [Ouvrir dans la boutique]({d.get('open_giveaway')})"
                        ),
                        "color": 0x7F00FF,
                        "footer": { "text": "by choukettas" },
                        "timestamp": datetime.utcnow().isoformat(),
                        "image": { "url": d.get("image") }
                    }
                ]
            }

            requests.post(webhook_url_DLC, json=payload)
            print(f"[OK] {d.get('title')} envoyé")

            with open("./data/epicgame_DLC.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

    except Exception as e:
        print("Erreur :", e)

    try:

        old_id = None
        if os.path.exists("./data/steam_DLC.json"):
            with open("./data/steam_DLC.json", "r", encoding="utf-8") as f:
                old_data = json.load(f)
                if isinstance(old_data, list) and old_data:
                    old_id = old_data[0].get("id")

        
        r = requests.get(url, params=params_steam_DLC, timeout=5)
        r.raise_for_status()
        data = r.json()

        if not data or not isinstance(data, list):
            print("⚠️ Données invalides")
            time.sleep(5)
            continue

        d = data[0]
        current_id = d.get("id")


        if old_id == current_id:
            print("⏩ Déjà envoyé, on ignore")

        else:
            print("🆕 Nouveau DLC détecté")

            payload = {
                "content": ping_target,
                "embeds": [
                    {
                        "thumbnail": { "url": "https://i.postimg.cc/hjrPkWbj/S2Qw-Qtm.png" },
                        "title": d.get("title"),
                        "description": (
                            f"{d.get('description')}\n\n"
                            f"~~{d.get('worth')}~~ **DLC jusqu’au {d.get('end_date')}**\n"
                            f"🔗 [Ouvrir dans la boutique]({d.get('open_giveaway')})"
                        ),
                        "color": 0x7F00FF,
                        "footer": { "text": "by choukettas" },
                        "timestamp": datetime.utcnow().isoformat(),
                        "image": { "url": d.get("image") }
                    }
                ]
            }

            requests.post(webhook_url_DLC,json=payload)
            print(f"[OK] {d.get('title')} envoyé")

            with open("./data/steam_DLC.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

    except Exception as e:
        print("Erreur :", e)

    time.sleep(300)
