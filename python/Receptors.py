## Receptors ##
## functions for working with receptors in Random-Walk-RPI
## Board Population function, coordinate transformations, and receptor state change

import numpy as np

# 'walker' is a walker object
# 'world' is an object that corresponds to the board
# and other global attributes of the problem

class World: # just a dummy class for debugging and testing
    def __init__(self, board):
        self.board = board

def seedReceptors(world, numReceptors, receptorSize=1):
    # function to return an array of ints with ones indicating the position of receptors and zeroes everywhere else

    worldDim = np.shape(world) # stores dimensions of board
    receptorArray = np.zeros(worldDim, dtype=np.int8) # initializes empty position matrix


    pos = np.zeros([len(worldDim),numReceptors],dtype=np.int8) # make empty array for positions
    j = 0 # j is an iterator over each dimension in worldDim

    for i in worldDim: # for each dimension
        pos[j,:] = np.random.randint(0,i,numReceptors) # make a list of random coordinates in that dimension for each receptor and append it to pos
        j += 1 # iterates over each dimension in worldDim

    # the pos matrix now contains all of the positions of receptors
    for i in pos.T:
        receptorArray[tuple(i)] = 1 # indicate positions of receptors with '1'
    receptorLogicArray=np.ravel((receptorArray!=0))
    return receptorLogicArray,pos

def indexToCoords(n,s,d,rank=2):
    #This function converts list index to matrix like coordinate
    #The last step is a transformation of matrix coordinate into coordinate plane
    i=0
    matcoord=np.zeros(rank,dtype=np.int8)
    while(i<rank):
       q=d**i
       matcoord[i] = ((n-(n%q))/q)%d
       i+=1
    #Converts matrix index to coordinate plane
    coord[0]=matcoord[0]-s
    coord[1]=s-matcoord[1]
    return coord

def coordsToIndex(coord,s,d,rank=2):
    #This function converts the coordinate system to a list index
    #There is an intermediate transformation into a matrix like coordinate
    k=0
    n=0
    matcoord=np.zeros(rank,dtype=np.int8)
    #Converts from coordinate plane to matrix index
    matcoord[0]=coord[0]+s
    matcoord[1]=s-coord[1]
    while(k<rank):
        n+=(d**k)*matcoord[k]
        k+=1
    return n

def sealPortal(coordinate,steps,worlddim,recpt):
    #This closes the receptors on the surface when the walker is an antagonist
    m=coordsToIndex(coordinate,steps,worlddim)
    recpt[m]={False:False,True:False}[recpt[m]]
    return recpt
