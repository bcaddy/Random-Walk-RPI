import numpy as np
import pylab
import random
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats
from scipy.stats import norm
rng = np.random.default_rng()
random.seed()

# single walk code 
# keeps track of each position

# parameters for walk
n = 10000 #number of steps
origin = np.zeros((1,2))
choices = [[1,0],[0,1],[-1,0],[0,-1]] #step directions that can be taken
prob = [1/4,1/4,1/4,1/4] #probability of corresponding step direction

# simulate walk in 2D
steps = rng.choice(choices, size=n, p=prob) #array of each step
path = np.concatenate([origin, steps]).cumsum(0) #cumulative summation of steps
start = path[0:1]
end = path[-1:]

# plot the path
fig = plt.figure(figsize=(7,7),dpi=300)
ax = fig.add_subplot()
ax.scatter(path[:,0], path[:,1],c='black',alpha=0.5,s=0.7);
ax.plot(path[:,0], path[:,1],c='blue',alpha=0.5,lw=0.5);
ax.plot(start[:,0], start[:,1],c='green',marker='o')
ax.plot(end[:,0], end[:,1],c='red',marker='o')
plt.gca().set_aspect('equal')
plt.tight_layout()
plt.title('random walk')
plt.xlabel('x')
plt.ylabel('y')
