# import libraries
import json
import numpy as np

# load the replay data from a single game
f = open('game.json')

# parse the replay data
data = json.load(f)

# print the names of the players on the blue team
#print(data['blue']['players'][0]['id']['id'])

# count number of demos by the team
blue_demos = print(data['blue']['stats']['demo']['inflicted'])
orange_demos = print(data['orange']['stats']['demo']['inflicted'])
