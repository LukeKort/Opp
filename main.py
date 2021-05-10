# Python code by Lucas Kort (May. 10, 2021)
# Main

import numpy as np
from parameters import n_iterations
from plotter_export_csv import plotter
from plotter_export_csv import export_csv

methods=['y','y'] #methods to be processed [Alcateia[y/n],Alcateia2[y/n]]
n_methods=methods.count('y')
result_table=np.zeros((n_iterations,n_methods))
i=0
methods_name=[]

if methods[0].lower() == 'y':
    from alcateia import best_result_acum
    result_table[:,i] = best_result_acum
    name='Alcateia'
    methods_name.append('Alcateia')
    i=i+1
if methods[1].lower() == 'y':
    from pso import best_result_acum
    result_table[:,i] = best_result_acum
    name='Particle Swarn'
    methods_name.append('Particle Swarn')
    i=i+1

plotter(result_table,n_methods,methods_name)
export_csv(result_table,methods_name)