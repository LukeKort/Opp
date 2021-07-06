# Main (Jun. 16, 2021)

from importlib import reload #to reload a previuly loaded file
from time import time #to count time
from datetime import datetime #to print date
import numpy as np #some arry operations
import sys 
import os #to open external programms
from PyQt5 import QtGui, QtCore, QtWidgets
import opp_gui
from plotter_export_csv import plotter

#Parameters
methods=['n','n','n'] #methods to be processed - start with none

class EmittingStream(QtCore.QObject): #print to consele QLineEdit
    textWritten = QtCore.pyqtSignal(str)
    def write(self, text):
        self.textWritten.emit(str(text))

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = opp_gui.Ui_MainWindow() # in this and next line you say that you will use all widgets from testUI over self.ui
        self.ui.setupUi(self)
        self.setWindowTitle('Opp RC') #set windows title Opp [--v]
        #so, when you say self.ui.myButton ,that is pushButton in testUI that has name myButton 
        self.ui.play_button.clicked.connect(self.run_methods)# connect button clicked with action
        self.ui.edit_function_button.clicked.connect(self.open_function)
        self.ui.help_button.clicked.connect(self.open_help)
        self.ui.youtube.clicked.connect(self.youtube)
        self.ui.alcateia.toggled.connect(self.alcateia_check)
        self.ui.pso.toggled.connect(self.pso_check)
        self.ui.jaakola.toggled.connect(self.lj_check)
        #self.ui.export_results_cvs.toggled.connect(self.export_check)

        # Install the custom output stream
        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)

    def __del__(self): #print to consele QLineEdit
        # Restore sys.stdout
        sys.stdout = sys.__stdout__

    def normalOutputWritten(self, text): #print to consele QLineEdit
        """Append text to the QTextEdit."""
        # Maybe QTextEdit.append() works as well, but this is how I do it:
        cursor = self.ui.console.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.ui.console.setTextCursor(cursor)
        self.ui.console.ensureCursorVisible()
    
    def open_function(self): #opens objective e constraints functions to user's edit
        fileName = 'functions.py'
        os.system("notepad.exe " + fileName) #open in especific programm
    
    def youtube(self): #opens help documentation
        import webbrowser
        url = 'https://youtu.be/Y79Re82K3W0'
        os.startfile(url)

    def open_help(self): #opens help documentation
        fileName = 'help_file.pdf'
        os.system("start " + fileName) #open in default program

    def alcateia_check(self):
        if self.ui.alcateia.isChecked():   
            methods[0]='y'
        else:
            methods[0]='n'

    def pso_check(self):
        if self.ui.pso.isChecked():   
            methods[1]='y'
        else:
            methods[1]='n'
    
    def lj_check(self):
        if self.ui.jaakola.isChecked():   
            methods[2]='y'
        else:
            methods[2]='n'
    
    ex_count = 1 #count the number of executions

    def run_methods(self): #run the methods

        print(datetime.now().strftime("%H:%M:%S"),"\n")

        try:
            import functions
            reload(functions)  #uptade the changes made in the function file
        except:
            print('Parece que existe um problema com as funções fornecidas.\n')
            return
        from functions import constraints
        from functions import objective

        n_iterations = int(self.ui.n_iterations.text())
        n_particles = int(self.ui.n_particles.text())
        tolerance = float(self.ui.n_tolerance.text())
        a = list(map(float,(self.ui.vector_inf_limit.text().split(',')))) #limit inferior per variable (must be a list)
        b= list(map(float,(self.ui.vector_sup_limit.text().split(',')))) #limit superior per variable (must be a list)
        n_variables = np.size(a) #number of variables = number of constraints
        pso_only_w=float(self.ui.w_pso_only.text()) #w for alcateia only
        pso_only_c1=float(self.ui.c1_pso_only.text()) #c1 for alcateia only
        pso_only_c2=float(self.ui.c2_pso_only.text()) #c2 for alcateia only
        alcateia_only_ic = int(self.ui.alcateia_inner_circle.text()) #internal cicles for alcateia only
        alcateia_only_id = float(self.ui.alcatei_id.text()) #idependency for alcateia only
        lj_only_in = int(self.ui.inner_circle_lj_only.text()) #internal for alcateia only
        lj_only_c = float(self.ui.c_lj_only.text()) #contraction factor(0,1) for alcateia only

        
        if np.size(a) != np.size(b): #check for erros in a and b
            print('O limite inferior e superior tem tamanhos diferentes!\n')
            return

        if alcateia_only_id < 0 or alcateia_only_id > 1: #check for erros in jaakola innercircles
            print("No Alcateia, o parâmetro 'id' precisa estar entre 0 e 1 \n")
            return

        if lj_only_c < 0 or lj_only_c > 1: #check for erros in jaakola innercircles
            print("No Jaakola, o parâmetro 'c'precisa estar entre 0 e 1 \n")
            return

        if n_iterations < 1 or n_particles < 1 or alcateia_only_ic < 1 or lj_only_in < 1: #check for erros in jaakola innercircles
            print("O número de iterações, laços internos e partículas precisam ser no mínimo 1 \n")
            return

        try: #check for erros in objective, constraints functions
            teste_var = np.ones((n_variables,1))
            constraints(teste_var)
            objective(teste_var)
        except:
            print('Função ou limites fornecidos não aceitos\n')
            return

        n_methods=methods.count('y')
        result_table=np.zeros((n_iterations,n_methods))
        last_iteration=np.zeros(n_methods) #consider early end of method's processing by tolerance
        i=0
        methods_name=[]

        if 'y' not in methods:
            print('Nenhum método foi selecionado!\n')
            return

        if methods[0] == 'y':
            from alcateia import alcateia
            alcateia_results=alcateia(n_particles,n_variables,n_iterations,tolerance,a,b,alcateia_only_ic,alcateia_only_id) #activate de alcateia method
            result_table[:,i] = alcateia_results['acumulate_result']
            last_iteration[i] = alcateia_results['max_n_iteration']
            methods_name.append('Alcateia')
            i=i+1
        if methods[1] == 'y':
            from pso import pso
            pso_results=pso(n_particles,n_variables,n_iterations,tolerance,a,b,pso_only_w,pso_only_c1,pso_only_c2) #activate de alcateia method
            result_table[:,i] = pso_results['acumulate_result']
            last_iteration[i] = pso_results['max_n_iteration']
            methods_name.append('Particle Swarm')
            i=i+1
        if methods[2] == 'y':
            from luus_jaakola import lj
            lj_results=lj(n_variables,n_iterations,tolerance,a,b,lj_only_in, lj_only_c) #activate de alcateia method
            result_table[:,i] = lj_results['acumulate_result']
            last_iteration[i] = lj_results['max_n_iteration']
            methods_name.append('Luus Jaakola')
            i=i+1

        plotter(n_iterations,last_iteration,result_table,n_methods,methods_name)
        
        if self.ui.export_results_cvs.isChecked():
            from plotter_export_csv import export_csv
            export_csv(result_table,methods_name,n_iterations)
            
            
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())