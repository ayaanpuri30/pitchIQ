import http.client

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': ""
    }

conn.request("GET", "/players/squads?team=33", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))