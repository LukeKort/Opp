# Test (May. 18, 2021) - used for test only
from luus_jaakola import lj
from alcateia import alcateia
from pso import pso
import numpy as np

n_iterations = 400
tolerance = 1e-20
n_particles = 400
a = [0]
b = [87600]
lj_only = [30,0] #laço interno, contração
alcateia_only_ic = 50
alcateia_only_id = 0.7
pso_only_w = 0.5
pso_only_c1 = pso_only_c2 = 1
n_variables = np.size(a)

for i in range(2):
    #lj(n_variables,n_iteration,tolerance,a,b,lj_only)
    pso(n_particles,n_variables,n_iterations,tolerance,a,b,pso_only_w,pso_only_c1,pso_only_c2)
    alcateia(n_particles,n_variables,n_iterations,tolerance,a,b,alcateia_only_ic,alcateia_only_id)