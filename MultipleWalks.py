import numpy as np
import pylab
import random
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats
from scipy.stats import norm
rng = np.random.default_rng()

# code for multiple simulations
# only cares for final positions

# function for calculating fit
def normal(mean, std, color="black"):
    a = np.linspace(mean-4*std, mean+4*std, 200)
    b = stats.norm.pdf(a, mean, std)
    c = plt.plot(a, b, color, linewidth=2)

# parameters for the walk
n = 10000 #number of steps per simulation
m = 10000 #number of simulations
origin = np.zeros((1,2))
choices = [[1,0],[0,1],[-1,0],[0,-1]] #step directions that can be taken
prob = [1/4,1/4,1/4,1/4] #probability of corresponding step direction

xfinal = np.zeros(m)
yfinal = np.zeros(m)

# Simulate steps in 2D
for i in range (1,m):
    random.seed()
    steps = rng.choice(choices, size=n, p=prob) #array of each step
    path = np.concatenate([origin, steps]).cumsum(0) #cumulative summation of steps
    start = path[0:1]
    end = path[-1:]
    
    xfinal[i] = end[0][0]
    yfinal[i] = end[0][1]
    
    
# plot the distribution of final position
sns.histplot(xfinal, stat = 'density', color = 'red')
normal(xfinal.mean(), xfinal.std())
pylab.show()

sns.histplot(yfinal, stat = 'density', color = 'blue')
normal(yfinal.mean(), yfinal.std())
pylab.show()
