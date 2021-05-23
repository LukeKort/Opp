# Test (May. 18, 2021) - used for test only
from luus_jaakola import lj
from alcateia import alcateia
from pso import pso
import numpy as np

n_iteration = 100
tolerance = 1e-20
n_particles = 200
a = [-600,-600]
b = [600,600]
lj_only = [30,0] #laço interno, contração
alcateia_only = [50,0.7]
pso_only = []
n_variables = np.size(a)

#lj(n_variables,n_iteration,tolerance,a,b,lj_only)
alcateia(n_particles,n_variables,n_iteration,tolerance,a,b,alcateia_only)