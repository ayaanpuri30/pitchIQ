import requests
from typing import List, Dict
HEADERS = {
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "b0bbb5c087e903cf1d5e6faed4658c06"
}
LEAGUES_URL = "https://api-football-v1.p.rapidapi.com/v3/leagues"
TEAMS_URL = "https://api-football-v1.p.rapidapi.com/v3/teams"
PLAYERS_URL="https://api-football-v1.p.rapidapi.com/v3/players"
def get_all_leagues() -> List[Dict]:
    """Call it to get all available leagues"""
    response = requests.get(LEAGUES_URL, headers=HEADERS)
    if response.status_code != 200:
        print(f"Error fetching leagues: {response.status_code}")
        return []
    data = response.json()
    leagues = [
        {
            "league_id": league["league"]["id"],
            "league_name": league["league"]["name"],
        }
        for league in data["response"]
    ]
    return leagues

FAVORITE_LEAGUES = {
    "Premier League": 39,
    "La Liga": 140,
    "Serie A": 135,
    "Bundesliga": 78,
    "Ligue 1": 61,
    "Eredivisie": 88,
    "UEFA Champions League": 2,
    "UEFA Europa League": 3,
    "UEFA Conference League": 4,
    "UEFA Super Cup": 5,
    "Championship": 180,
    "Primeira Liga": 94,
}


def get_all_teams(leagues_dict: Dict[str, int] = FAVORITE_LEAGUES) -> pd.DataFrame:
    """Get all teams from a list of leagues and save them to a CSV file"""
    all_teams = []
    for (
        league_name,
        league_id,
    ) in leagues_dict.items():
        print(f"Fetching teams for league: {league_name} (ID: {league_id})")
        league_teams = get_teams_from_league(int(league_id), league_name)
        if len(league_teams) < 10:
            continue
        all_teams.append(league_teams)
    all_teams_df = pd.concat(all_teams)
    all_teams_df.to_csv("teams.csv", index=False)


def get_player_data(player_name: str, team_name: str, season=2024) -> pd.DataFrame:
    """Get player stats using player name and his current team"""
    team_id = get_team_id(team_name)
    if not team_id:
        print(f"Team '{team_name}' not found")
        return None
    player_id = get_player_id(team_id, player_name)
    if player_id is None:
        return None
    player_stats = get_player_stats(player_id, team_id, season)
    return player_stats

player_name="Ricardo Esgaio"
team="Sporting CP"
player_df=get_player_data(player_name,team)
player_df.head()