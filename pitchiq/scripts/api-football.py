import http.client

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "b0bbb5c087e903cf1d5e6faed4658c06"
    }

conn.request("GET", "/players/squads?team=33", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))