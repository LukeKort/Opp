# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'opp.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1110, 640)
        MainWindow.setMinimumSize(QtCore.QSize(1110, 640))
        MainWindow.setMaximumSize(QtCore.QSize(1110, 640))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Opp_title = QtWidgets.QLabel(self.centralwidget)
        self.Opp_title.setGeometry(QtCore.QRect(10, -10, 181, 121))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.Opp_title.setFont(font)
        self.Opp_title.setObjectName("Opp_title")
        self.help_button = QtWidgets.QPushButton(self.centralwidget)
        self.help_button.setGeometry(QtCore.QRect(1040, 10, 51, 41))
        self.help_button.setStyleSheet("border-image: url(:/icons_images/icons/help_button.png);")
        self.help_button.setText("")
        self.help_button.setObjectName("help_button")
        self.console = QtWidgets.QTextEdit(self.centralwidget)
        self.console.setGeometry(QtCore.QRect(760, 70, 321, 381))
        self.console.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.console.setObjectName("console")
        self.edit_function_button = QtWidgets.QPushButton(self.centralwidget)
        self.edit_function_button.setGeometry(QtCore.QRect(780, 490, 161, 71))
        self.edit_function_button.setAcceptDrops(False)
        self.edit_function_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-image: url(:/icons_images/icons/edit_function_icon.png);")
        self.edit_function_button.setText("")
        self.edit_function_button.setObjectName("edit_function_button")
        self.play_button = QtWidgets.QPushButton(self.centralwidget)
        self.play_button.setGeometry(QtCore.QRect(980, 480, 81, 81))
        self.play_button.setMouseTracking(False)
        self.play_button.setStyleSheet("border-image: url(:/icons_images/icons/start_button.png);")
        self.play_button.setText("")
        self.play_button.setDefault(True)
        self.play_button.setObjectName("play_button")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 130, 201, 431))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.verticalLayoutWidget_4.setFont(font)
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.alcateia = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.alcateia.setFont(font)
        self.alcateia.setAcceptDrops(False)
        self.alcateia.setToolTip("")
        self.alcateia.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.alcateia.setAutoExclusive(False)
        self.alcateia.setObjectName("alcateia")
        self.verticalLayout_4.addWidget(self.alcateia)
        self.pso = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.pso.setFont(font)
        self.pso.setAcceptDrops(False)
        self.pso.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pso.setAutoExclusive(False)
        self.pso.setObjectName("pso")
        self.verticalLayout_4.addWidget(self.pso)
        self.grad_desc_stoc = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.grad_desc_stoc.setFont(font)
        self.grad_desc_stoc.setAcceptDrops(False)
        self.grad_desc_stoc.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.grad_desc_stoc.setAutoExclusive(False)
        self.grad_desc_stoc.setObjectName("grad_desc_stoc")
        self.verticalLayout_4.addWidget(self.grad_desc_stoc)
        self.jaakola = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.jaakola.setFont(font)
        self.jaakola.setAcceptDrops(False)
        self.jaakola.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.jaakola.setAutoExclusive(False)
        self.jaakola.setObjectName("jaakola")
        self.verticalLayout_4.addWidget(self.jaakola)
        self.pca = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.pca.setFont(font)
        self.pca.setAcceptDrops(False)
        self.pca.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pca.setAutoExclusive(False)
        self.pca.setObjectName("pca")
        self.verticalLayout_4.addWidget(self.pca)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(310, 100, 411, 492))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.horizontalLayoutWidget.setFont(font)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.particles_lb = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.particles_lb.setFont(font)
        self.particles_lb.setObjectName("particles_lb")
        self.verticalLayout_2.addWidget(self.particles_lb)
        self.tolerance_lb = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.tolerance_lb.setFont(font)
        self.tolerance_lb.setObjectName("tolerance_lb")
        self.verticalLayout_2.addWidget(self.tolerance_lb)
        self.iterations_lb = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.iterations_lb.setFont(font)
        self.iterations_lb.setObjectName("iterations_lb")
        self.verticalLayout_2.addWidget(self.iterations_lb)
        self.inf_limit_lb = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.inf_limit_lb.setFont(font)
        self.inf_limit_lb.setObjectName("inf_limit_lb")
        self.verticalLayout_2.addWidget(self.inf_limit_lb)
        self.sup_limit_lb = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.sup_limit_lb.setFont(font)
        self.sup_limit_lb.setObjectName("sup_limit_lb")
        self.verticalLayout_2.addWidget(self.sup_limit_lb)
        self.alcateia_only_lb = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.alcateia_only_lb.setFont(font)
        self.alcateia_only_lb.setObjectName("alcateia_only_lb")
        self.verticalLayout_2.addWidget(self.alcateia_only_lb)
        self.pso_only_lb = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.pso_only_lb.setFont(font)
        self.pso_only_lb.setObjectName("pso_only_lb")
        self.verticalLayout_2.addWidget(self.pso_only_lb)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.n_particles = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.n_particles.setFont(font)
        self.n_particles.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.n_particles.setObjectName("n_particles")
        self.verticalLayout_3.addWidget(self.n_particles)
        self.n_tolerance = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.n_tolerance.setFont(font)
        self.n_tolerance.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.n_tolerance.setObjectName("n_tolerance")
        self.verticalLayout_3.addWidget(self.n_tolerance)
        self.n_iterations = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.n_iterations.setFont(font)
        self.n_iterations.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.n_iterations.setObjectName("n_iterations")
        self.verticalLayout_3.addWidget(self.n_iterations)
        self.vector_inf_limit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.vector_inf_limit.setFont(font)
        self.vector_inf_limit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.vector_inf_limit.setObjectName("vector_inf_limit")
        self.verticalLayout_3.addWidget(self.vector_inf_limit)
        self.vector_sup_limit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.vector_sup_limit.setFont(font)
        self.vector_sup_limit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.vector_sup_limit.setObjectName("vector_sup_limit")
        self.verticalLayout_3.addWidget(self.vector_sup_limit)
        self.vector_alcateia_only = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.vector_alcateia_only.setFont(font)
        self.vector_alcateia_only.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.vector_alcateia_only.setObjectName("vector_alcateia_only")
        self.verticalLayout_3.addWidget(self.vector_alcateia_only)
        self.vector_pso_only = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.vector_pso_only.setFont(font)
        self.vector_pso_only.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.vector_pso_only.setObjectName("vector_pso_only")
        self.verticalLayout_3.addWidget(self.vector_pso_only)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.version_number = QtWidgets.QLabel(self.centralwidget)
        self.version_number.setGeometry(QtCore.QRect(200, 70, 31, 19))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(False)
        font.setWeight(50)
        self.version_number.setFont(font)
        self.version_number.setObjectName("version_number")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1110, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Opp_title.setText(_translate("MainWindow", "Opp."))
        self.alcateia.setText(_translate("MainWindow", "Alcateia"))
        self.pso.setText(_translate("MainWindow", "PSO"))
        self.grad_desc_stoc.setText(_translate("MainWindow", "GDS"))
        self.jaakola.setText(_translate("MainWindow", "Jaakola"))
        self.pca.setText(_translate("MainWindow", "PCA"))
        self.particles_lb.setText(_translate("MainWindow", "Particles"))
        self.tolerance_lb.setText(_translate("MainWindow", "Tolerance"))
        self.iterations_lb.setText(_translate("MainWindow", "Iterations"))
        self.inf_limit_lb.setText(_translate("MainWindow", "Inf limit"))
        self.sup_limit_lb.setText(_translate("MainWindow", "Sup limit"))
        self.alcateia_only_lb.setText(_translate("MainWindow", "Alcateia [cicles, id]"))
        self.pso_only_lb.setText(_translate("MainWindow", "PSO [w, c1, c2]"))
        self.version_number.setText(_translate("MainWindow", "0.2"))

import icon_rc

#I had to add this manually from https://stackoverflow.com/questions/45043904/pyqt5-gui-runs-with-no-errors-but-window-doesnt-appear
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())