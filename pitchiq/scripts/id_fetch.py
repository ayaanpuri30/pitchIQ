import requests
import json
import time
API_TOKEN = "K5ZQYl6ziNvlrCBGfg8izoLSY7cnhaoHIHnEemowX9Bbdm1uoiKybJ8vdpIW"
cur_page = 1
BASE_URL = f"https://api.sportmonks.com/v3/football/teams?api_token="+API_TOKEN+"&per_page=50"

teams_data = []
response = requests.get(BASE_URL)
response.raise_for_status()
data = response.json()
teams_data.append(data['data'])
while data['pagination']['has_more']:
    time.sleep(0.5)
    cur_page += 1
    URL = f"https://api.sportmonks.com/v3/football/teams?api_token="+API_TOKEN+f"&per_page=50&page={cur_page}"
    response = requests.get(URL)
    response.raise_for_status()
    data = response.json()
    teams_data.append(data['data'])

with open("team_ids.json", 'w') as f:
    json.dump({"data" : teams_data}, f, indent=4)
#print(data)
