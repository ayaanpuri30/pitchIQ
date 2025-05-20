import requests
import os
import json
import time

API_TOKEN = ""

BASE_URL_SQUAD = "https://api.sportmonks.com/v3/football/squads/teams"
BASE_URL_PLAYER = "https://api.sportmonks.com/v3/football/players"
BASE_URL_TEAM = "https://api.sportmonks.com/v3/football/teams"  # NEW for team (club) data
BASE_URL_COACH = "https://api.sportmonks.com/v3/football/coaches"

position_map = {
    1: "Goalkeeper",
    2: "Defender",
    3: "Midfielder",
    4: "Forward",
    24: "Goalkeeper",
    25: "Defender",
    26: "Midfielder",
    27: "Forward"
}

clubs = [
    "Manchester City", "Liverpool", "Manchester United",
    "Atl\u00e9tico Madrid", "Real Madrid", "FC Barcelona",
    "Paris Saint Germain", "LOSC Lille", "Olympique Marseille"
]

with open("team_ids.json", "r") as f:
    team_map_big = json.load(f)

team_map = {item['name']: item['id'] for item in team_map_big["data"]}

output_folder = "pitchiq/src/clubData"
os.makedirs(output_folder, exist_ok=True)

def fetch_squad(team_id):
    url = f"{BASE_URL_SQUAD}/{team_id}?api_token={API_TOKEN}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def fetch_player(player_id):
    url = f"{BASE_URL_PLAYER}/{player_id}?api_token={API_TOKEN}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def fetch_club(team_id):
    url = f"{BASE_URL_TEAM}/{team_id}?api_token={API_TOKEN}&include=coaches"  # include coach data
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
def fetch_coach(coach_id):
    url = f"{BASE_URL_COACH}/{coach_id}?api_token={API_TOKEN}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch coach {coach_id}: {response.status_code}")
        return None
def main():
    for team_name, team_id in team_map.items():
        if team_name not in clubs:
            continue
        print(f"Fetching {team_name} data...")


        filename = os.path.join(output_folder, f"{team_name.replace(' ', '_')}.tsx")

        # Fetch data
        squad_data = fetch_squad(team_id)
        club_data = fetch_club(team_id)

        # Process players
        new_squad = []
        for player_entry in squad_data["data"]:
            player_id = player_entry["player_id"]
            try:
                player_info = fetch_player(player_id)
                player_data = player_info["data"]
                new_player = {
                    "id": player_id,
                    "name": player_data["display_name"],
                    "age": player_data.get("date_of_birth", "N/A"),
                    "number": player_entry.get("jersey_number", None),
                    "position": position_map.get(player_data["position_id"], "Unknown"),
                    "photo": player_data["image_path"]
                }
                new_squad.append(new_player)
                time.sleep(0.5)  # Avoid rate limit
            except Exception as e:
                print(f"Failed to fetch player {player_id}: {e}")
                continue

        # Extract club info
        club_info = club_data["data"]
        coaches_list = club_info.get("coaches", [])
        coach_info = coaches_list[-1] if coaches_list else {}
        coach_info = fetch_coach(coach_info["coach_id"])['data']

        # Build final data structure
        club_object = {
            "club_name": club_info["name"],
            "club_logo": club_info["image_path"],
            "manager_name": coach_info.get("name", "Unknown"),
            "manager_photo": coach_info.get("image_path", None),
            "squad": new_squad
        }

        # Save to TSX
        var_name = team_name.replace(" ", "").replace("-", "").replace(".", "")
        tsx_content = f"const {var_name}Data = {json.dumps(club_object, indent=2)};\n\nexport default {var_name}Data;\n"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(tsx_content)

        print(f"Saved {filename}")

if __name__ == "__main__":
    main()
