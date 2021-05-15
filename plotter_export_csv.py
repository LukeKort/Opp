# Plotter charts and export to CVS files (May. 12, 2021)

import matplotlib.pyplot as plt
import pandas as pd
from tkinter import filedialog
from mpl_toolkits.axisartist.axislines import Axes

def plotter(x_limit,last_iteration,y_var,n_methods,name):
    
    fig = plt.figure(figsize=(6,4)) #chart size
    
    for i in range(n_methods):
        iterations_limit = int(last_iteration[i]) #consider early end of method's processing by tolerance
        plt.scatter(range(iterations_limit),y_var[0:iterations_limit,i],alpha=0.5,label=name[i])
  
    plt.title('Best function value')
    plt.ylabel('Function value')
    plt.xlabel('Iteration')
    plt.legend()
    plt.xlim([0,x_limit])
    plt.show()

def export_csv(table,header,index_col):
    df_results=pd.DataFrame(table,index=range(index_col),columns=header)
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    try:
        df_results.to_csv(export_file_path)
    except:
        print('No file path was given!')