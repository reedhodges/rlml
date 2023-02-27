import requests
import json

url = 'https://ballchasing.com/api/replays'

G2_params = {'player-id':['steam:76561198293785594','steam:76561198293785594','steam:76561198994386260'], 'count':'50', 'playlist': 'private'}
auth = {'Authorization':'TOKEN'}

r = requests.get(url, params=G2_params, headers=auth)

# save output to json file
with open('output.json', 'w') as outfile:
    json.dump(r.json(), outfile)