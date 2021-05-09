import numpy as np
from parameters import ext_cicles
from plotter_export_csv import plotter

methods=['y','y'] #methods to be processed [Alcateia[y/n],Alcateia2[y/n]]
n_methods=np.size(methods)
result_table=np.zeros((ext_cicles,n_methods))
i=0
methods_name=[]

if methods[0].lower() == 'y':
    from alcateia import best_result_acum
    result_table[:,i] = best_result_acum
    methods_name.append('Alcateia')
    i=i+1
if methods[1].lower() == 'y':
    from pso import best_result_acum
    result_table[:,i] = 2*best_result_acum
    methods_name.append('PSO')
    i=i+1

plotter(result_table,n_methods)