# Python code by Lucas Kort (May. 05, 2021)
# Objectives and constraints functions
import math

def objective(var): #objetive functions
    x1=var[0] #variables 1 to n
    x2=var[1]
   
    y=math.sin(x1)*math.exp((1-math.cos(x2))**2) + math.cos(x2)*math.exp((1-math.sin(x1))**2) + (x1-x2)**2 #function(s)
    
    return y #result

def constraints(var): #constraint functions
    x1=var[0] #variables 1 to n
    x2=var[1]

    y1 = (x1+5)**2 + (x2+5)**2 #constraint functions 1 to n
    y2 = 0

    if (y1 ==0) and (y2 == 0): #test conditions 1 to n
        return True #all conditions has been met
    else:
        return False #one or more condition hasn't been met