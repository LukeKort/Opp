# Python code by Lucas Kort (May. 10, 2021)
# Parameters

import random as rand
import numpy as np

n_particles = 100
a= [-10,-10] #limit inferior per variable (must be a list)
b= [0, 0] #limit superior per variable (must be a list)
n_variables = np.size(a) #number of variables = number of constraints
n_iterations = 50
pso_only=[0.5,2,2] #[w,c1,c2] - for PSO only
alcateia_only = [20,0.7] #[internal cicles, idependency] - for alcateia only 
tolerance = 0

def radom_generator(x,y,a,b): #generates a x for y vector between the limits a and b with real values
    vector = np.zeros((x,y),dtype=float)
    for i in range(x):
        for j in range(y):
            vector[i,j] = a[i]+(b[i]-a[i])*rand.random()
    return vector