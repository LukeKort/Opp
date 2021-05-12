# Python (May. 12, 2021)
# Particle Swarn

import time
import numpy as np
import random as rand
from random_matrix import radom_generator #random generator. takes x and y vector dimentions between the limits a and b
from functions import objective #objetive function(s)
from functions import constraints #constraint function(s)

def pso(n_particles,n_variables,n_iterations,tolerance,a,b,pso_only):
    results = np.ones((n_particles)) #preallocation
    best_result_acum = np.zeros((n_iterations)) #preallocation
    x_aux = x = np.zeros((n_variables, n_particles)) #x_aux stores the best value's position per particle/x is the first position matrix
    v = radom_generator(n_variables,n_particles,a,b) #velocity matrix
    x_best = np.zeros((n_variables))

    t_0 = time.time() #start time

    for i in range(n_iterations):  
        x_0=x.copy() #stores the last x before uptade
        for j in range(n_particles):
            v[:,j]= pso_only[0]*v[:,j] + rand.random()*pso_only[1]*(x_aux[:,j]-x[:,j]) + rand.random()*pso_only[2]*(x_best - x[:,j]) #new velocity matrix
            x[:,j]=x_0[:,j]+v[:,j] #new position matrix
            for k in range(n_variables): #test with the limits (a,b)
                if x[k,j]<a[k]:
                    x[k,j]=rand.randrange(a[k],b[k])
                if x[k,j]>b[k]:
                    x[k,j]=rand.randrange(a[k],b[k])
            if (constraints(x[:,j])) is True: #teste the new x within the constraints functions
                if (objective(x[:,j])) < objective(x_aux[:,j]): #teste the new x within the objetive function
                    x_aux[:,j] = x[:,j] #setting new best particle position
            results[j] = objective(x_aux[:,j]) #save result per particle
        best_result = min(results) #find best result of all particles
        best_result_acum[i] = best_result
        idx = results.tolist().index(best_result) #find the best result's index inside the results vector
        x_best = x_aux[:,idx] #find the best result's position
        
        if tolerance >= np.amax(abs(x-x_0)): #break for setting tolerance
            break

    t_end = time.time() #finish time
    t_total = t_end - t_0 #total processing time

    print('#Particle Swarn\nThe best result is:',best_result,'\nLocated at:',x_best,'\nProcessing time:',(t_total),'s\n')
    
    return({'best_result':best_result,'acumulate_result':best_result_acum,'x_best':x_best,'t_total':t_total})