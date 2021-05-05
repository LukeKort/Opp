# Python code by Lucas Kort (May. 04, 2021)
# Método Alcateia
import time
import numpy as np
import random as rand
from parameters import n_particles #default parameters import - number of particles
from parameters import n_variables #default parameters import - number of variables
from parameters import int_cicles #default parameters import - number of internal cicles
from parameters import ext_cicles #default parameters import - number of external cicles
from parameters import tolerance #default parameters import - tolerance limit
from parameters import a #default parameters import - functions' domain inferior limit 
from parameters import b #default parameters import - functions' domain superior limit 
from parameters import radom_generator #random generator. takes x and y vector dimentions between the limits a and b
from functions import objective #objetive(s) function(s)
from functions import constraints

x = delta = np.zeros((n_variables,n_particles), dtype=float) #preallocation
results = np.ones((n_particles)) #preallocation
r = radom_generator(n_variables,n_particles,a,b)
x_0 = (radom_generator(n_variables,n_particles,a,b))

t_0 = time.time() #start time

for i in range(ext_cicles): #external cicle
    x_aux = x_0
    for j in range(int_cicles): #internal cicle
        for k in range(n_particles): #calculos per particle
            delta[:,k]=(-1+2*rand.random())*r[:,k]
            x[:,k]=x_0[:,k]+delta[:,k] #particle update
            if (constraints(x[:,k])) is True: #teste within the constraints functions
                if (objective(x[:,k])) < objective(x_0[:,k]): #teste particle update
                    x_0[:,k] = x[:,k] #setting new particle position
            results[k] = objective(x_0[:,k]) #save result per particle
    best_result = min(results) #find best result of all particles
    idx = results.tolist().index(best_result) #find the best result's index inside the results vector
    x_best = x_0[:,idx] #find the best result's position
    for w in range(n_particles): #uptade x_0 within the best result of last external cicle
        x_0[:,w] = rand.random()*x_0[:,w]+(1-rand.random())*x_best
        r[:,w] = abs(x_0[:,w] - x_aux[:,w])

    if tolerance <= np.amax(r): #break for setting tolerance
          break

t_end = time.time() #finish time
t_total = t_end - t_0 #total processing time

print('The best result is:',best_result,'\nLocated at:',x_best,'\nProcessing time:',(t_total),'s')