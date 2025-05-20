import requests
import json
import time

API_TOKEN = "K5ZQYl6ziNvlrCBGfg8izoLSY7cnhaoHIHnEemowX9Bbdm1uoiKybJ8vdpIW"
BASE_URL_COACH = "https://api.sportmonks.com/v3/football/coaches"

# Example: list of coach IDs you want to check
coach_ids = [
    455800
    # add your coach IDs here
]

def fetch_coach(coach_id):
    url = f"{BASE_URL_COACH}/{coach_id}?api_token={API_TOKEN}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch coach {coach_id}: {response.status_code}")
        return None

def main():
    for coach_id in coach_ids:
        print(f"Fetching coach {coach_id}...")
        data = fetch_coach(coach_id)
        if data and "data" in data:
            coach_data = data["data"]
            print(json.dumps(coach_data, indent=2))  # Pretty print the coach info
        else:
            print(f"No data for coach {coach_id}")
        time.sleep(0.5)  # small sleep to be polite to API

if __name__ == "__main__":
    main()
