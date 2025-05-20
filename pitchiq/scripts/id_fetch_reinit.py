import requests
import json
import time
with open("team_ids.json", "r") as f:
    team_map_big = json.load(f)
li = team_map_big["data"]
to_go = []
for l in li:
    to_go.extend(l)
team_map = {"data" : to_go}
with open("team_ids.json", "w") as f:
    json.dump(team_map, f, indent=4)