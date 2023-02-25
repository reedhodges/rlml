# import libraries
import json
import numpy as np
import matplotlib.pyplot as plt
import os   # for getting file names
from gradient_descent import grad_desc_LR   

# load and parse the replay data from the RLCS Winter Regional 2 Main Event
# no data from OCE winter regional 2 because it had a corrupted file
cwd = os.getcwd()  # get current working directory
subdir = 'replays'  # subdirectory where replay data is stored
file_names = os.listdir(os.path.join(cwd, subdir))  # get file names
data = []
for file_name in file_names:
    with open(os.path.join(cwd, subdir, file_name), 'r') as f:
        json_data = json.load(f)
        data.append(json_data)

# win percentage
win_percentage = []
# demos inflicted per game
demos_inflicted_per_game = []
# boost stolen
boost_stolen = []
for i in range(0, len(data)):
    for j in range(0, len(data[i]["teams"])):
        if data[i]["teams"][j]["cumulative"]["games"] > 5:  # min 5 games played
            win_percentage.append(data[i]["teams"][j]["cumulative"]["win_percentage"])
            demos_inflicted_per_game.append(data[i]["teams"][j]["game_average"]["demo"]["inflicted"])
            boost_stolen.append(data[i]["teams"][j]["game_average"]["boost"]["amount_stolen"])
        else:
            pass

# fit data to linear regression model
# rescaled values of boost stolen to be between 0 and 100 to match win percentage
fit = grad_desc_LR([(x-700)/(20-7) for x in boost_stolen], win_percentage, 1, 1, 0.00001, 10000)

# rescale the slope and intercept to get the actual values
slope = fit.slopeintercept()[0]/(20-7)
intercept = fit.slopeintercept()[1] - 700*slope

# print values of slope and intercept
print("slope: ", slope)
print("intercept: ", intercept)

# plot data with linear fit
plt.scatter(boost_stolen, win_percentage, color='red')
plt.scatter([i for i in range(500,2200,10)], [slope*i+intercept for i in range(500,2200,10)])
plt.show()