# Objectives and constraints functions (May. 05, 2021)
import math
import numpy as np

# from numpy.cor_t.fromnumeric import around

def objective(var_o): #objetive functions

    #confiabilidade

    gamma_ = 3.000122547
    theta = 30.63657894

    t = int(math.floor(var_o.copy()))

    r_t = math.exp(-((t/theta)**(gamma_)))
        
    #custo

    c_m = 1000
    c_r = 2500
    c_inc = 10000
    t_ser = 87600
    mttf = 27.8067216

    c_t = (t_ser/t)*c_m*r_t + (t_ser/mttf)*(c_r+c_inc)*(1-r_t)  
    
    #função objetivo

    y = c_t

    return y

def constraints(var_c): #constraint functions

    #confiabilidade
    
    gamma_ = 3.000122547
    theta = 30.63657894

    lim = 0.950

    t = int(math.floor(var_c.copy()))

    r_t = math.exp(-((t/theta)**(gamma_)))

    #disponibilidade

    t_m = 0.5       #tempo de r_tparo
    t_r = 2     #tempo de manutenção

    a_t = t/(t + r_t*t_m + (1-r_t)*t_r)

   
    #constraint functions 1 to n
    if (r_t >= lim): #test conditions 1 to n
        return True #all conditions has been met
    else:
        return False #one or mor_t condition hasn't been met