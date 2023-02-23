# import libraries
import json
import numpy as np
import matplotlib.pyplot as plt

# load and parse the replay data from the RLCS Winter Regional 2 Main Event
# no data from OCE winter regional 2 because it had a corrupted file
file_names = ['fall1apac.json', 'fall1apac.json', 'fall1eur.json', 'fall1mena.json', 'fall1na.json', 'fall1oce.json', 'fall1sa.json', 'fall1ssa.json', 'fall2apac.json', 'fall2eur.json', 'fall2mena.json', 'fall2na.json', 'fall2oce.json', 'fall2sa.json', 'fall2ssa.json', 'fall3apac.json', 'fall3eur.json', 'fall3mena.json', 'fall3na.json', 'fall3oce.json', 'fall3sa.json', 'fall3ssa.json', 'winter1apac.json', 'winter1eur.json', 'winter1mena.json', 'winter1na.json', 'winter1oce.json', 'winter1sa.json', 'winter1ssa.json', 'winter2apac.json', 'winter2eur.json', 'winter2mena.json', 'winter2na.json', 'winter2sa.json', 'winter2ssa.json']
data = []
for file_name in file_names:
    with open(file_name) as f:
        json_data = json.load(f)
        data.append(json_data)

# win percentage
win_percentage = []
for i in range(0, len(data)):
    for j in range(0, len(data[i]["teams"])):
        win_percentage.append(data[i]["teams"][j]["cumulative"]["win_percentage"])

# demos inflicted per game
demos_inflicted_per_game = []
for i in range(0, len(data)):
    for j in range(0, len(data[i]["teams"])):
        demos_inflicted_per_game.append(data[i]["teams"][j]["game_average"]["demo"]["inflicted"])

print(len(demos_inflicted_per_game))

plt.scatter(demos_inflicted_per_game, win_percentage)
plt.show()