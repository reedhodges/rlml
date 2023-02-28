import requests
import json

url = 'https://ballchasing.com/api/replays'
auth = {'Authorization':'TOKEN'}

# JKnaps: 76561198061585314
# Chicago: 76561198293785594
# Atomic: 76561198994386260
player_ids = {'player-id':['steam:76561198061585314','steam:76561198293785594','steam:76561198994386260']}
game_count = {'count':'50'}
playlist = {'playlist':'private'}

search_params = player_ids + game_count + playlist

r = requests.get(url, params=search_params, headers=auth)

# save output to json file
with open('output.json', 'w') as outfile:
    json.dump(r.json(), outfile)