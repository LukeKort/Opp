# Main (May. 12, 2021)

import numpy as np
import sys
from plotter_export_csv import plotter
from plotter_export_csv import export_csv
from functions import constraints
from functions import objective

#Parameters
methods=['y','y','y'] #methods to be processed [Alcateia[y/n],Alcateia2[y/n]]
n_particles = 100
a= [-10,-10] #limit inferior per variable (must be a list)
b= [0, 0] #limit superior per variable (must be a list)
n_variables = np.size(a) #number of variables = number of constraints
n_iterations = 100
pso_only=[0.5,2,2] #[w,c1,c2] - for PSO only
alcateia_only = [20,0.7] #[internal cicles, idependency] - for alcateia only
lj_only = [500,0.005] #[internal cicles,contraction factor(0,1)] - for alcateia only
tolerance = 0

try: #check for erros in objective, constraints functions
    teste_var = np.ones((n_variables,1))
    constraints(teste_var)
    objective(teste_var)
except:
    sys.exit('Function not correctly inputted\n')

n_methods=methods.count('y')
result_table=np.zeros((n_iterations,n_methods))
i=0
methods_name=[]

if methods[0].lower() == 'y':
    from alcateia import alcateia
    alcateia_results=alcateia(n_particles,n_variables,n_iterations,tolerance,a,b,alcateia_only) #activate de alcateia method
    result_table[:,i] = alcateia_results['acumulate_result']
    #name='Alcateia'
    methods_name.append('Alcateia')
    i=i+1
if methods[1].lower() == 'y':
    from pso import pso
    pso_results=pso(n_particles,n_variables,n_iterations,tolerance,a,b,pso_only) #activate de alcateia method
    result_table[:,i] = pso_results['acumulate_result']
    #name='Particle Swarm'
    methods_name.append('Particle Swarm')
    i=i+1
if methods[2].lower() == 'y':
    from luus_jaakola import lj
    lj_results=lj(n_variables,n_iterations,tolerance,a,b,lj_only) #activate de alcateia method
    result_table[:,i] = lj_results['acumulate_result']
    #name='Particle Swarm'
    methods_name.append('Luus Jaakola')
    i=i+1

plotter(n_iterations,result_table,n_methods,methods_name)
export_csv(result_table,methods_name,n_iterations)