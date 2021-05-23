# Objectives and constraints functions (May. 05, 2021)
import math

def objective(var): #objetive functions
    
    x1 = var[0]
    x2 = var[1]


    frac1 = 1 + math.cos(12*math.sqrt(x1**2+x2**2))
    frac2 = 0.5*(x1**2+x2**2) + 2

    y = -frac1/frac2 #function(s)
    
    return y #result

def constraints(var): #constraint functions
    x1=var[0] #variables 1 to n
    x2=var[1]

    y1 = 0 #constraint functions 1 to n
    y2 = 0

    if (y1 == 0): # and (y2 == 0): #test conditions 1 to n
        return True #all conditions has been met
    else:
        return False #one or more condition hasn't been met