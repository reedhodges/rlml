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
# demos inflicted per game
demos_inflicted_per_game = []
for i in range(0, len(data)):
    for j in range(0, len(data[i]["teams"])):
        if data[i]["teams"][j]["cumulative"]["games"] > 5:  # min 5 games played
            win_percentage.append(data[i]["teams"][j]["cumulative"]["win_percentage"])
            demos_inflicted_per_game.append(data[i]["teams"][j]["game_average"]["demo"]["inflicted"])
        else:
            pass

# program to implement gradient descent for linear regression
class grad_desc_LR:
    def __init__(self, x, y, m_init, b_init, alpha, num_iter):
        self.x = x                
        self.y = y
        self.m_init = m_init          # initial slope
        self.b_init = b_init          # initial intercept
        self.alpha = alpha          # learning rate
        self.num_iter = num_iter    # number of iterations

    def slopeintercept(self):
        m = self.m_init
        b = self.b_init
        for i in range(self.num_iter):
            # update slope and intercept using previous values, so need temporary variables
            for j in range(len(self.x)):
                m_tmp = m - self.alpha / len(self.x) * self.x[j] * (m * self.x[j] + b - self.y[j])
                b_tmp = b - self.alpha / len(self.x) * (m * self.x[j] + b - self.y[j])
                m = m_tmp
                b = b_tmp
        return [m, b]
    
fit = grad_desc_LR(demos_inflicted_per_game, win_percentage, 15, 40, 0.0001, 10000)
slope = fit.slopeintercept()[0]
intercept = fit.slopeintercept()[1]

print("slope: " + str(slope))
print("intercept: " + str(intercept))

plt.scatter(demos_inflicted_per_game, win_percentage)
plt.show()