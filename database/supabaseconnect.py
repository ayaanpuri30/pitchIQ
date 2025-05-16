import json
from glob import glob
from supabase import create_client, Client
from postgrest import APIError
from scripts import *

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "soccerdata")
PATTERN = os.path.join(DATA_DIR, "*", "Heatmaps", "Quarter3.png")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
FIXED_TEAM_NAME = "Atlético Madrid"

for img_path in sorted(glob(PATTERN)):
    print("Processing:", img_path)

    match_dir = os.path.basename(os.path.dirname(os.path.dirname(img_path)))
    print("match_dir:", match_dir)

    if " - " not in match_dir:
        print(f"Folder name doesn’t contain ' - ': {match_dir} (skipping)")
        continue

    date_str, _ = match_dir.split(" - ", 1)
    try:
        match_id = int(date_str.replace("-", ""))
    except ValueError:
        print(f"Invalid date in folder: {date_str} (skipping)")
        continue

    # 1) compute zones
    try:
        zone_json = compute_zone_from_image(img_path, CONFIG)
    except Exception as e:
        print(f"Failed to compute zones: {e}")
        continue

    # 2) GPT summary
    try:
        summary = get_playstyle_description(zone_json)
    except Exception as e:
        print(f"GPT failed: {e}")
        continue

    # 3) insert
    row = {
        "match_id": match_id,
        "team_name": FIXED_TEAM_NAME,
        "zone_json": zone_json,
        "gpt_summary": summary
    }
    try:
        supabase.table("playstyle_summaries").insert(row).execute()
        print(f"Inserted {match_id} | {FIXED_TEAM_NAME}")
    except APIError as e:
        print(f"Supabase error: {e}")
