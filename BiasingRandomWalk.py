# Biased Random Walk
# Program to perform a biased random walk

# import packages
import numpy as np
import matplotlib.pyplot as plt
import random
import seaborn as sns
import pylab
from scipy import stats
from scipy.stats import norm

# define variables
nwalkers = 1000
ndims = 2
nsteps = 1000
finalpos = np.zeros([nwalkers,ndims]) # stores final positions of walkers
stepweights = [2,1,2,1] # stores weights of possible steps
steps = [[1,0],[-1,0],[0,1],[0,-1]] # stores possible steps

for i in range(0,nwalkers): # for each walker
    
    pos = np.zeros([1,ndims]) # set position to zero
    
    for j in range (1,nsteps): # for each step
        pos += random.choices(steps,stepweights) # update the position using a randomly chosen step
        
    finalpos[i,:] = pos

# define normal to compare histogram to
def normal(mean, std, color="black"):
    a = np.linspace(mean-4*std, mean+4*std, 200)
    b = stats.norm.pdf(a, mean, std)
    c = plt.plot(a, b, color, linewidth=2)

# display results
sns.histplot(finalpos[:,0], stat='density', color='red')
normal(finalpos[:,0].mean(), finalpos[:,0].std())
pylab.show()

sns.histplot(finalpos[:,1], stat='density', color='blue')
normal(finalpos[:,1].mean(), finalpos[:,1].std())
pylab.show()
