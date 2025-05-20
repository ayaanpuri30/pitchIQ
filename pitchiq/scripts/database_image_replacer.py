"""Goes through every player/coach in the database and replaces their image with the nicer one from FotMob."""

from supabase import create_client, Client
from fotmob_scraper import Scraper

SUPABASE_URL = "https://rcrngkqsybnjfgyvhnyu.supabase.co"
SUPABASE_KEY = ""

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
scraper = Scraper()

# Update coach images
clubs_resp = supabase.table("clubs").select("club_name, manager_name, manager_photo").execute()
clubs = clubs_resp.data

for club in clubs:
    manager_name = club["manager_name"]
    if club["manager_photo"] != None:
        continue
    better_img = scraper.scrape(manager_name, save_to_file=False)

    if better_img:
        supabase.table("clubs").update({
            "manager_photo": better_img
        }).eq("club_name", club["club_name"]).execute()
        print(f"✅ Updated coach {manager_name}'s image.")

# Update player images
players_resp = supabase.table("players").select("player_id, name, photo").execute()
players = players_resp.data
player_count = len(players)
count = 1
for player in players:
    player_name = player["name"]
    better_img = scraper.scrape(player_name)
    if player["photo"] != None:
        count += 1
        continue
    if better_img:
        supabase.table("players").update({
            "photo": better_img
        }).eq("player_id", player["player_id"]).execute()
        print(f"✅ Updated player {player_name}'s image. {(count/player_count)*100:.2f}% completed.")
        count += 1
    else:
        print(f"❌ No image found for player: {player_name}")

print("All images updated successfully.")
scraper.shut_down() # Need to quit the driver
