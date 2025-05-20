"""
THIS FILE PERFORMS THE SAME TASK/FUNCTIONALITY AS database_sync_psycopg2.py, BUT USES A DIFFERENT SQL AUTH SYSTEM.
INSTEAD OF USING psycopg2, IT USES THE SUPABASE PYTHON WRAPPER TO CONNECT AND WORK WITH THE SUPABASE POSTGRESSQL DATABASE.

Note: Databases cant be created using this method, can only be updated, accessed, fetched, etc.
"""


import json

from glob import glob
from supabase import create_client, Client

#template path for where club data will be stored
CLUB_DATA_PATH = "pitchiq/src/clubData/*.json"

SUPABASE_URL = "https://rcrngkqsybnjfgyvhnyu.supabase.co"
SUPABASE_KEY = ""

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# process JSON files containing current iter of data
for filepath in glob(CLUB_DATA_PATH):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"Processing club {data['club_name']}...")

    # UPSERT club
    supabase.table("clubs").upsert([{
        "club_name": data["club_name"],
        "club_logo": data["club_logo"],
        "manager_name": data["manager_name"],
        "manager_photo": data["manager_photo"]
    }]).execute()

    # UPSERT squad
    player_rows = []
    for player in data["squad"]:
        player_rows.append({
            "player_id": player["id"],
            "club_name": data["club_name"],
            "name": player["name"],
            "birthdate": player["age"] if player["age"] else None,
            "number": player["number"],
            "position": player["position"],
            "photo": player["photo"]
        })

    if player_rows:
        supabase.table("players").upsert(player_rows).execute()

print("Database synced successfully via Supabase REST API.")
