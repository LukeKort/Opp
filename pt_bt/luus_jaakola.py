# Luus Jaakola (Jun. 29, 2021)

import time
import numpy as np
import random as rand
from importlib import reload #to reload a previuly loaded file

def lj(n_variables,n_iterations,tolerance,a,b,lj_only_in, lj_only_c):

    from random_matrix import radom_generator #random generator. takes x and y vector dimentions between the limits a and b
    import functions
    reload(functions)  #uptade the changes made in the function file
    from functions import objective #objetive function(s)
    from functions import constraints #constraint function(s)

    best_result_acum = np.empty((n_iterations)) #preallocation
    x_0 = (radom_generator(n_variables,1,a,b)) #postion matrix
    x = r= np.ones((n_variables,1))

    t_0 = time.time() #start time

    for i in range(n_iterations): #external cicle
        x_aux = x_0.copy()
        for j in range(lj_only_in): #internal cicle
            x[:,0]=x_0[:,0]+(2*rand.random()-1)*r[:,0] #particle update
            if (constraints(x[:,0])) is True: #teste within the constraints functions
                if (objective(x[:,0])) < objective(x_0[:,0]): #teste particle update
                    x_0 = x #setting new particle position
        
        best_result = objective(x_0[:,0]) #find best result of each iteration
        best_result_acum[i] = best_result
        
        r[:,0] = (1-lj_only_c)*abs(x[:,0] - x_aux[:,0])
        
        if tolerance >= np.amax(r): #break for setting tolerance
            x_best = x_0 #find the best result's position
            break

    x_best = x_0[:,0] #find the best result's position

    t_end = time.time() #finish time
    t_total = t_end - t_0 #total processing time

    print('#Luus Jaakola\nMelhor resultado:',best_result,'\nPosição:',x_best,'\nTempo de execução:',(t_total),'s\n')

    return({'best_result':best_result,'acumulate_result':best_result_acum,'x_best':x_best,'t_total':t_total,'max_n_iteration':i})