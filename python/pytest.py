import Receptors
import numpy as np
rng=np.random.default_rng()

n=10
group_size=10
path = rng.choice([[1,0],[-1,0],[0,1],[0,-1]],size=group_size)
#receptors = np.zeros((n,n))
#receptors,positionlist = Receptors.seedReceptors(receptors,30)

steps = rng.choice([[1,0],[-1,0],[0,1],[0,-1]], size=group_size)  # array of currently generated steps
add_on = steps.cumsum(0) + path[-1, 0:2]
check = add_on[:,:]
print(path)
print(steps)
print(check)
