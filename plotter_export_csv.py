# Python code by Lucas Kort (May. 10, 2021)
# Plotter charts and export to CVS files

import matplotlib.pyplot as plt
import pandas as pd
from tkinter import filedialog
from mpl_toolkits.axisartist.axislines import Axes
from parameters import n_iterations

def plotter(var,n_methods,name):
    
    fig = plt.figure(figsize=(6,4)) #chart size
    
    for i in range(n_methods):
        plt.scatter(range(n_iterations),var[:,i],alpha=0.5,label=name[i])
  
    plt.title('Best function value')
    plt.ylabel('Function value')
    plt.xlabel('Iteration')
    plt.legend()
    plt.xlim([0,n_iterations])
    plt.show()

def export_csv(table,header):
    df_results=pd.DataFrame(table,index=range(n_iterations),columns=header)
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    try:
        df_results.to_csv(export_file_path)
    except:
        print('No file path was given!')