# import libraries
import json
import numpy as np
import matplotlib.pyplot as plt

# load and parse the replay data from the RLCS Winter Regional 2 Main Event
# no data from OCE winter regional 2 because it had a corrupted file
f1 = open('fall1apac.json')
f2 = open('fall1eur.json')
f3 = open('fall1mena.json')
f4 = open('fall1na.json')
f5 = open('fall1oce.json')
f6 = open('fall1sa.json')
f7 = open('fall1ssa.json')
f8 = open('fall2apac.json')
f9 = open('fall2eur.json')
f10 = open('fall2mena.json')
f11 = open('fall2na.json')
f12 = open('fall2oce.json')
f13 = open('fall2sa.json')
f14 = open('fall2ssa.json')
f15 = open('fall3apac.json')
f16 = open('fall3eur.json')
f17 = open('fall3mena.json')
f18 = open('fall3na.json')
f19 = open('fall3oce.json')
f20 = open('fall3sa.json')
f21 = open('fall3ssa.json')
f22 = open('winter1apac.json')
f23 = open('winter1eur.json')
f24 = open('winter1mena.json')
f25 = open('winter1na.json')
f26 = open('winter1oce.json')
f27 = open('winter1sa.json')
f28 = open('winter1ssa.json')
f29 = open('winter2apac.json')
f30 = open('winter2eur.json')
f31 = open('winter2mena.json')
f32 = open('winter2na.json')
f34 = open('winter2sa.json')
f35 = open('winter2ssa.json')

data1 = json.load(f1)
data2 = json.load(f2)
data3 = json.load(f3)
data4 = json.load(f4)
data5 = json.load(f5)
data6 = json.load(f6)
data7 = json.load(f7)
data8 = json.load(f8)
data9 = json.load(f9)
data10 = json.load(f10)
data11 = json.load(f11)
data12 = json.load(f12)
data13 = json.load(f13)
data14 = json.load(f14)
data15 = json.load(f15)
data16 = json.load(f16)
data17 = json.load(f17)
data18 = json.load(f18)
data19 = json.load(f19)
data20 = json.load(f20)
data21 = json.load(f21)
data22 = json.load(f22)
data23 = json.load(f23)
data24 = json.load(f24)
data25 = json.load(f25)
data26 = json.load(f26)
data27 = json.load(f27)
data28 = json.load(f28)
data29 = json.load(f29)
data30 = json.load(f30)
data31 = json.load(f31)
data32 = json.load(f32)
data34 = json.load(f34)
data35 = json.load(f35)

# win percentage
win_percentage = []
for i in range(0, len(data1["teams"])):
    win_percentage.append(data1["teams"][i]["cumulative"]["win_percentage"])
for i in range(0, len(data2["teams"])):
    win_percentage.append(data2["teams"][i]["cumulative"]["win_percentage"])
for i in range(0, len(data3["teams"])):
    win_percentage.append(data3["teams"][i]["cumulative"]["win_percentage"])
for i in range(0, len(data4["teams"])):
    win_percentage.append(data4["teams"][i]["cumulative"]["win_percentage"])
for i in range(0, len(data5["teams"])):
    win_percentage.append(data5["teams"][i]["cumulative"]["win_percentage"])
for i in range(0, len(data6["teams"])):
    win_percentage.append(data6["teams"][i]["cumulative"]["win_percentage"])
for i in range(0, len(data7["teams"])):
    win_percentage.append(data7["teams"][i]["cumulative"]["win_percentage"])
for i in range(0, len(data8["teams"])):
    win_percentage.append(data8["teams"][i]["cumulative"]["win_percentage"])
for i in range(0, len(data9["teams"])):
    win_percentage.append(data9["teams"][i]["cumulative"]["win_percentage"])
for i in range(0, len(data10["teams"])):
    win_percentage.append(data10["teams"][i]["cumulative"]["win_percentage"])

# demos inflicted per game
demos_inflicted_per_game = []
for i in range(0, len(data1["teams"])):
    demos_inflicted_per_game.append(data1["teams"][i]["game_average"]["demo"]["inflicted"])
for i in range(0, len(data2["teams"])):
    demos_inflicted_per_game.append(data2["teams"][i]["game_average"]["demo"]["inflicted"])
for i in range(0, len(data3["teams"])):
    demos_inflicted_per_game.append(data3["teams"][i]["game_average"]["demo"]["inflicted"])
for i in range(0, len(data4["teams"])):
    demos_inflicted_per_game.append(data4["teams"][i]["game_average"]["demo"]["inflicted"])
for i in range(0, len(data5["teams"])):
    demos_inflicted_per_game.append(data5["teams"][i]["game_average"]["demo"]["inflicted"])
for i in range(0, len(data6["teams"])):
    demos_inflicted_per_game.append(data6["teams"][i]["game_average"]["demo"]["inflicted"])
for i in range(0, len(data7["teams"])):
    demos_inflicted_per_game.append(data7["teams"][i]["game_average"]["demo"]["inflicted"])
for i in range(0, len(data8["teams"])):
    demos_inflicted_per_game.append(data8["teams"][i]["game_average"]["demo"]["inflicted"])
for i in range(0, len(data9["teams"])):
    demos_inflicted_per_game.append(data9["teams"][i]["game_average"]["demo"]["inflicted"])
for i in range(0, len(data10["teams"])):
    demos_inflicted_per_game.append(data10["teams"][i]["game_average"]["demo"]["inflicted"])

print(len(demos_inflicted_per_game))

plt.scatter(demos_inflicted_per_game, win_percentage)
plt.show()