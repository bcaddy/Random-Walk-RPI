## Receptors ##
## functions for working with receptors in Random-Walk-RPI

import numpy as np

# 'walker' is a walker object
# 'world' is an object that corresponds to the board
# and other global attributes of the problem

class World: # just a dummy class for debugging and testing
    def __init__(self, board):
        self.board = board

myWorld = World(np.zeros([2,3,4])) # create dummy object for testing

def seedReceptors(world, numReceptors, receptorSize):
    # function to return an array of ints with ones indicating the position of receptors and zeroes everywhere else

    
    worldDim = np.shape(myWorld.board) # stores dimensions of board
    receptorArray = np.zeros(worldDim, dtype=np.int8) # initializes empty position matrix


    pos = np.zeros([len(worldDim),numReceptors],dtype=np.int8) # make empty array for positions
    j = 0 # j is an iterator over each dimension in worldDim

    for i in worldDim: # for each dimension
        pos[j,:] = np.random.randint(0,i,numReceptors) # make a list of random coordinates in that dimension for each receptor and append it to pos
        j += 1 # iterates over each dimension in worldDim

    # the pos matrix now contains all of the positions of receptors
    for i in pos.T:
        receptorArray[tuple(i)] = 1 # indicate positions of receptors with '1'

    return receptorArray

    
    
    
