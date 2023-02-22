# import libraries
import json

# load the replay data from a single game
f = open('game.json')

# parse the replay data
data = json.load(f)

# print the names of the players on the blue team
print(data['blue']['players'][0]['id']['id'])
print(data['blue']['players'][1]['id']['id'])
print(data['blue']['players'][2]['id']['id'])

# print the names of the players on the orange team
print(data['orange']['players'][0]['id']['id'])
print(data['orange']['players'][1]['id']['id'])
print(data['orange']['players'][2]['id']['id'])

