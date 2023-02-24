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

# class to implement gradient descent for linear regression
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
            # initialize sums to 0
            [sum_m, sum_b] = [0, 0]
            for j in range(len(self.x)):
                sum_m += self.x[j] * (m * self.x[j] + b - self.y[j])
                sum_b += m * self.x[j] + b - self.y[j]
            # update slope and intercept using previous values, so need temporary variables
            m_tmp = m - (self.alpha * sum_m) / len(self.x)
            b_tmp = b - (self.alpha * sum_b) / len(self.x)
            [m, b] = [m_tmp, b_tmp]
        return [m, b]

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