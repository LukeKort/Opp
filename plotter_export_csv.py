# Python code by Lucas Kort (May. 06, 2021)
# Plotter charts and export to CVS files
from mpl_toolkits.axisartist.axislines import Axes
import matplotlib.pyplot as plt

def plotter(var,n_methods):
    
    fig = plt.figure(figsize=(4,3)) #chart size
    
    for i in range(n_methods):
        plt.plot(var[:,i])
  
    plt.title('Best value per cicle')
    plt.ylabel('Y values')
    plt.xlabel('number of cicles')
    plt.show()