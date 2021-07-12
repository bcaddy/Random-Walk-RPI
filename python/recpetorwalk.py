import numpy as np
import math
import Receptors
rng=np.random.default_rng()

#Random Walk Control Parameters
dim=2
mu=0.237614141414 #"Chemical Potential"
nantag=200    #number of walker antagonists
nwalker=1000  #number of walkers
mantag=1000   #number of steps for antagonists
mwalker=1000  #        ""      for walkers
axis_x = 2*m+1 #range of the axis for x and y
board = np.zeros((axis_x,axis_x)) #initialize the board
boardfill=math.floor(np.random.normal(loc=((2*m+1)**2)/2,scale=mu)) #randomly samples Gaussian to determine number of receptors
adest = np.array((0,2))
antagseal = np.array((0,2))

wdest = np.array((0,2))


def simulation(nsteps, recarray, origin=[0,0], group=10, prob=[0.25,0.25,0.25,0.25]):
        
        # Does the actual random walk simulation.
        # The total number of steps to be taken by the walker is divided into groups of size group_size.
        # A list of weighted steps are generated within each grouping,given a list of weights, one after the other. 
        # The function then checks if any of the steps in the currently generated grouping will result in an overlap with a receptor. 
        # If there is an overlap, the walker is stopped with this as the final position of its path. If no overlap is found,
        # the function adds these steps to the path and generates another grouping of steps to test. This continues until 
        # the desired number of steps is reached, being nsteps
        bins=nsteps//group
        choices=[[1,0],[0,1],[0,-1],[-1,0]]
        for i in range(bins):
            steps = rng.choice(choices, size=group, p=prob)  # array of currently generated steps
            add_on = steps.cumsum(0) + path[-1, 0:2]

            for j in range(group):
                check=Receptors.coordstoIndex(add_on[j])
                if(recarray[check]):
                    reccoord = add_on[j,:]  # receptor that walker intercepted with
                    fadd_on = add_on[:j+1,:]
                    path = np.concatenate([path, fadd_on])
                    return(path, reccoord)
                else:
                    continue 
            path = np.concatenate([path, add_on])
            
        reccoord = None  # receptor set to None if walker does not intercept any during simulation
        return(path, reccoord)

#Populate the board with receptors
recarray,board=Receptors.seedReceptors(board,boardfill)
#Antagonists run the board
for i in range(nantag):
    history,reccoord = simulation(mantag,recarray)
    if(reccoord is not None):
        recarray = Receptors.sealPortal(reccoord,mantag,axis_x,recarray)
        antagseal[i,:] = 
    else:
        adest.append(history[-1,:],axis=0)
#Now we let the walkers run the board
for i in range(nwalker):
    history,reccoord = simulation(mwalker,recarray)
