# Alcateia (May. 12, 2021)

import time
import numpy as np
import random as rand
from random_matrix import radom_generator #random generator. takes x and y vector dimentions between the limits a and b
from functions import objective #objetive function(s)
from functions import constraints #constraint function(s)

def alcateia(n_particles,n_variables,n_iterations,tolerance,a,b,alcateia_only):
    x = delta = np.zeros((n_variables,n_particles), dtype=float) #preallocation
    results = np.ones((n_particles)) #preallocation
    best_result_acum = np.empty((n_iterations)) #preallocation

    r = radom_generator(n_variables,n_particles,a,b)
    x_0 = (radom_generator(n_variables,n_particles,a,b)) #postion matrix

    t_0 = time.time() #start time

    for i in range(n_iterations): #external cicle
        x_aux = x_0.copy()
        for j in range(alcateia_only[0]): #internal cicle
            for k in range(n_particles): #calculos per particle
                delta[:,k]=(-1+2*rand.random())*r[:,k]
                x[:,k]=x_0[:,k]+delta[:,k] #particle update
                if (constraints(x[:,k])) is True: #teste within the constraints functions
                    if (objective(x[:,k])) < objective(x_0[:,k]): #teste particle update
                        x_0[:,k] = x[:,k] #setting new particle position
                results[k] = objective(x_0[:,k]) #save result per particle
        best_result = min(results) #find best result of all particles
        best_result_acum[i] = best_result
        idx = results.tolist().index(best_result) #find the best result's index inside the results vector
        x_best = x_0[:,idx] #find the best result's position

        for w in range(n_particles): #uptade x_0 within the best result of last external cicle
            r[:,w] = abs(x_0[:,w] - x[:,w])
            x_0[:,w] = alcateia_only[1]*x_0[:,w]+(1-alcateia_only[1])*x_best
        
        if tolerance >= np.amax(r): #break for setting tolerance
            #best_result_acum[:,i:n_iterations]=best_result #comple the rest of the vector with the last value
            break

    t_end = time.time() #finish time
    t_total = t_end - t_0 #total processing time

    print('#Alcateia\nThe best result is:',best_result,'\nLocated at:',x_best,'\nProcessing time:',(t_total),'s\n')

    return({'best_result':best_result,'acumulate_result':best_result_acum,'x_best':x_best,'t_total':t_total,'max_n_iteration':i})