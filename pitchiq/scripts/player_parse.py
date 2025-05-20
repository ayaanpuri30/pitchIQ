import requests
from bs4 import BeautifulSoup
import json
import re
def get_understat_player_id(name):
    url = f"https://understat.com/search/players/{name}"
    res = requests.get(url)
    data = res.json()
    if not data['players']:
        raise ValueError("Player not found.")
    return data['players'][0]  # can print list if multiple players found

player = get_understat_player_id("lionel messi")
print(player)
# Example: Messi (id = 2140)
url = "https://understat.com/player/{player}}"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

# Find the script tag that contains 'matchesData'
scripts = soup.find_all("script")

for script in scripts:
    if "matchesData" in script.text:
        json_text = re.search(r"var matchesData\s+=\s+JSON\.parse\('(.*?)'\);", script.text, re.DOTALL)
        if json_text:
            json_str = json_text.group(1).encode('utf-8').decode('unicode_escape')
            matches_data = json.loads(json_str)
            break
else:
    raise ValueError("Could not find matchesData in any script tag.")

# Sample output (e.g., first match)
print(matches_data[0])
