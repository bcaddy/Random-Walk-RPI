import numpy as np
import matplotlib.pyplot as plt
import pylab
import math
import Receptors
rng=np.random.default_rng()

#Random Walk Control Parameters
dim=2
mu=0.014862391#"Chemical Potential"
nantag=1000   #number of walker antagonists
nwalker=1000  #number of walkers
mantag=100    #number of steps for antagonists
mwalker=100   #        ""      for walkers
axis_x = 2*(mantag)+1 #range of the axis for x and y
board = np.zeros((axis_x,axis_x)) #initialize the board
boardfill=math.floor(np.random.normal(loc=0.05*(axis_x**2),scale=mu)) #randomly samples Gaussian to determine number of receptors
adest = np.array([[0,0]])
antagseal = np.array([[0,0]])
wsucceed = np.array([[0,0]])
wdest = np.array([[0,0]])


def simulation(nsteps, axis, recarray, origin=[[0,0]], group=10, prob=[0.25,0.25,0.25,0.25]):
        
        # Does the actual random walk simulation.
        # The total number of steps to be taken by the walker is divided into groups of size group_size.
        # A list of weighted steps are generated within each grouping,given a list of weights, one after the other. 
        # The function then checks if any of the steps in the currently generated grouping will result in an overlap with a receptor. 
        # If there is an overlap, the walker is stopped with this as the final position of its path. If no overlap is found,
        # the function adds these steps to the path and generates another grouping of steps to test. This continues until 
        # the desired number of steps is reached, being nsteps
        bins=nsteps//group
        choices=[[1,0],[0,1],[0,-1],[-1,0]]
        path=np.array(origin)
        for i in range(bins):
            steps = rng.choice(choices, size=group, p=prob)  # array of currently generated steps
            add_on = steps.cumsum(0)+path[-1,:]

            for j in range(group):
                check=Receptors.coordsToIndex(add_on[j],nsteps,axis)
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
    history,reccoord = simulation(mantag,axis_x,recarray)
    if(reccoord is not None):
        recarray = Receptors.sealPortal(reccoord,mantag,axis_x,recarray)
        antagseal = np.insert(antagseal,-1,history[-1:,:],axis=0)
    else:
        adest = np.insert(adest,-1,history[-1,:],axis=0)

#Now we let the walkers run the board
for i in range(nwalker):
    history,reccoord = simulation(mwalker,axis_x,recarray)
    if(reccoord is not None):
        wsucceed=np.insert(wsucceed,-1,history[-1,:],axis=0)
    else:
        wdest=np.insert(wdest,-1,history[-1,:],axis=0)
#Delete the initializing entry in the arrays
antagseal=np.delete(antagseal,-1,0)
adest=np.delete(adest,-1,0)
wsucceed=np.delete(wsucceed,-1,0)
wdest=np.delete(wdest,-1,0)

fig, view = plt.subplots(2,2,figsize=(10,10))
view[0,0].scatter(board[0,:],board[1,:])
view[0,1].scatter(antagseal[:,0],antagseal[:,1])
view[1,1].scatter(adest[:,0],adest[:,1])
view[1,0].scatter(wsucceed[:,0],wsucceed[:,1])
view[1,0].scatter(wdest[:,0],wdest[:,1])
plt.show()
