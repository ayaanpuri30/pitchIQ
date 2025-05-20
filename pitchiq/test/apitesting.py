import soccerdata as sd
fotmob = sd.FotMob(leagues='ESP-La Liga', seasons='2022/2023')
match_stats = fotmob.read_team_match_stats(opponent_stats=False, team='Valencia')
match_stats.head()