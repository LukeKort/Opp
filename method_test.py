# Test (May. 18, 2021) - used for test only
from luus_jaakola import lj
from alcateia import alcateia
from pso import pso
import numpy as np

n_iteration = 100
tolerance = 0
a = [-10,-10]
b = [0,0]
lj_only = [30,0] #laço interno, contração
alcateia_only = []
pso_only = []
n_variables = np.size(a)

lj(n_variables,n_iteration,tolerance,a,b,lj_only)
