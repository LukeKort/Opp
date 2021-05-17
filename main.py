# Main (May. 12, 2021)

import numpy as np
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
import opp_gui
from plotter_export_csv import plotter
from plotter_export_csv import export_csv

#Parameters
methods=['n','n','n'] #methods to be processed - start with none

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = opp_gui.Ui_MainWindow() # in this and next line you say that you will use all widgets from testUI over self.ui
        self.ui.setupUi(self) 
        #so, when you say self.ui.myButton ,that is pushButton in testUI that has name myButton 
        self.ui.play_button.clicked.connect(self.run_methods)# connect button clicked with action
        self.ui.edit_function_button.clicked.connect(self.open_function)
        self.ui.alcateia.toggled.connect(self.alcateia_check)
        self.ui.pso.toggled.connect(self.pso_check)
        self.ui.jaakola.toggled.connect(self.lj_check)

    def open_function(self): #opens objective e constraints functions to user's edit
        import os
        fileName = 'functions.py'
        os.system("notepad.exe " + fileName)
    
    def alcateia_check(self):
        methods[0]='y'

    def pso_check(self):
        methods[1]='y'
    
    def lj_check(self):
        methods[2]='y'
    
    def run_methods(self): #run the methods

        from functions import constraints
        from functions import objective

        n_particles = 100
        a= [-10,-10] #limit inferior per variable (must be a list)
        b= [0, 0] #limit superior per variable (must be a list)
        n_variables = np.size(a) #number of variables = number of constraints
        n_iterations = 100
        pso_only=[0.5,2,2] #[w,c1,c2] - for PSO only
        alcateia_only = [20,0.7] #[internal cicles, idependency] - for alcateia only
        lj_only = [500,0.005] #[internal cicles,contraction factor(0,1)] - for alcateia only
        tolerance = 0

        try: #check for erros in objective, constraints functions
            teste_var = np.ones((n_variables,1))
            constraints(teste_var)
            objective(teste_var)
        except:
            sys.exit('Function not correctly inputted\n')

        n_methods=methods.count('y')
        result_table=np.zeros((n_iterations,n_methods))
        last_iteration=np.zeros(n_methods) #consider early end of method's processing by tolerance
        i=0
        methods_name=[]

        if methods[0].lower() == 'y':
            from alcateia import alcateia
            alcateia_results=alcateia(n_particles,n_variables,n_iterations,tolerance,a,b,alcateia_only) #activate de alcateia method
            result_table[:,i] = alcateia_results['acumulate_result']
            last_iteration[i] = alcateia_results['max_n_iteration']
            methods_name.append('Alcateia')
            i=i+1
        if methods[1].lower() == 'y':
            from pso import pso
            pso_results=pso(n_particles,n_variables,n_iterations,tolerance,a,b,pso_only) #activate de alcateia method
            result_table[:,i] = pso_results['acumulate_result']
            last_iteration[i] = pso_results['max_n_iteration']
            methods_name.append('Particle Swarm')
            i=i+1
        if methods[2].lower() == 'y':
            from luus_jaakola import lj
            lj_results=lj(n_variables,n_iterations,tolerance,a,b,lj_only) #activate de alcateia method
            result_table[:,i] = lj_results['acumulate_result']
            last_iteration[i] = lj_results['max_n_iteration']
            methods_name.append('Luus Jaakola')
            i=i+1

        plotter(n_iterations,last_iteration,result_table,n_methods,methods_name)
        export_csv(result_table,methods_name,n_iterations)
    
    #def open_function(self):
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())