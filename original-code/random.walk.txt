# Python code for 2D random walk.
import numpy as np
import pylab
import random
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_style('darkgrid')

  
# defining the number of steps
n = 400
xfinal = np.zeros(n)
yfinal = np.zeros(n)


#creating two array for containing x and y coordinate
#of size equals to the number of size and filled up with 0's

  
for k in range (1,400):
    x = np.zeros(n)
    y = np.zeros(n)
    
    # filling the coordinates with random variables
    for i in range(1, n):

        for j in range (1, i):
            num = random.random()
            if num >= 0 and num < 0.25:
                val = 1
            elif num >= 0.25 and num < 0.5:
                val = 2
            elif num >= 0.5 and num < 0.75:
                val = 3
            else:
                val = 4

            if val == 1:
                x[i] = x[i - 1] + 1
                y[i] = y[i - 1]
            elif val == 2:
                x[i] = x[i - 1] - 1
                y[i] = y[i - 1]
            elif val == 3:
                x[i] = x[i - 1]
                y[i] = y[i - 1] + 1
            else:
                x[i] = x[i - 1]
                y[i] = y[i - 1] - 1
                
    xfinal[k] = x[i]
    yfinal[k] = y[i]  
            

        
# plotting stuff:
#pylab.title("Random Walk ($n = " + str(n) + "$ steps)")
#pylab.plot(x, y)

# histogram and fit

sns.histplot(xfinal, kde=True)
pylab.show()

sns.histplot(yfinal, kde=True)
pylab.show()