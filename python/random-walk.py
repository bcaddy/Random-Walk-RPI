# Python code for 2D random walk.
import numpy as np
import pylab
import random
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats
from scipy.stats import norm

sns.set_style('darkgrid')

#defining function for fitting pf plot
def normal(mean, std, color="black"):
    a = np.linspace(mean-4*std, mean+4*std, 200)
    b = stats.norm.pdf(a, mean, std)
    c = plt.plot(a, b, color, linewidth=2)


# defining the number of steps
d = 2      # number of dimensions of the walk
n = 1000   # nmber of runs
m = 1000   # number of steps per run
lr=[-1,1]  # step option for random walk
wfinal=np.zeros((n,d))

#Below we produce n walks of m steps with directional weights randomly
#chosen and off set from 50% x-axis and 50% y-axis step in the overall walk

for k in range (1,n):
    nv = np.random.choice(m)*np.random.choice(lr) #sets a choice weight
    p1=(m+nv)//2 #Number of steps in x is offset from m/2
    p2=(m-nv)//2 #Number of steps in y is offset from m/2
    #Here we assign arrays based on the number of steps assigned to each direction
    rmerge1 = np.zeros(p1)
    rmerge2 = np.zeros(p2)
    steps1 = np.random.choice(lr,p1) #x steps are randomly chosen
    steps2 = np.random.choice(lr,p2) #y steps are randomly chosen
    #Arrays are merged into a single total array
    walker1=np.stack((rmerge1,steps1),axis=1)
    walker2=np.stack((steps2,rmerge2),axis=1)
    totalwalk=np.append(walker1,walker2,axis=0)
    #The array is shuffled and now the motion is randomized
    np.random.shuffle(totalwalk)
    dest=np.sum(totalwalk,axis=0)
    #
    wfinal[k,:]=dest[:]
        
# plotting stuff:


# histogram and fit

#sns.distplot(xfinal, fit=norm, kde=False)
sns.histplot(wfinal[:,0], stat = 'density', color = 'red')
normal(wfinal[:,0].mean(), wfinal[:,0].std())
pylab.show()

sns.histplot(wfinal[:,1], stat = 'density', color = 'blue')
normal(wfinal[:,1].mean(), wfinal[:,1].std())
pylab.show()
