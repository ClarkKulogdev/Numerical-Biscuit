from typing import Counter
from sympy.utilities import exceptions
from mainwindow import Ui_Numerical_Analysis
from Equation import Expression
from sympy import *
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, function_exponentiation, implicit_multiplication
from sympy import simplify
import sys

from fixed_iteration import fixed_point_method as fi
from bisection_method import bisection_method as bb
from false_point import false_point_method as fp
from newton_raphson import newton_raphson_method as nr
from secant_method import secant_method as sec

from PyQt5 import QtWidgets as qtw 
from PyQt5 import QtCore as qtc 
from PyQt5.QtWidgets import QLabel, QCheckBox, QWidget, QItemDelegate, QStyledItemDelegate, QAbstractItemDelegate, QItemDelegate

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

class Mainwindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.ui = Ui_Numerical_Analysis()
        self.ui.setupUi(self)
        ###when click go to function fixed_iteration
        self.ui.fi_button_solve.clicked.connect(self.fixed_iteration) 

        ###when click go to function bisection
        self.ui.b_button_solve.clicked.connect(self.bisection)
        
        ###When click go to function false point
        self.ui.fp_button_solve.clicked.connect(self.false_point)
        
        #when click go to function Newton Raphson
        self.ui.nr_button_solve.clicked.connect(self.newton_raphson)
        
        #When click go to function secant method
        self.ui.secant_button_solve.clicked.connect(self.secant_method)
                
    def fixed_iteration(self):
        
        ### Validating the input first
        status_qoo = False
        ###declaring variable x
        x = Symbol('x')
        try:
            ###gonna get the input equation
            test_equation = self.ui.fi_input_fx.text()
            ###parsing the equation
            fx_equation = parse_expr(test_equation)
            ###i input sa una ang g(x) kay lisod
            test_equation = self.ui.fi_input_gx.text()
            gx_equation = parse_expr(test_equation)
            # testing to display the equations
            print(fx_equation)
            print(gx_equation)
            
            ### gonna check if the initial guess is a float
            initial_x = float(self.ui.fi_input_x.text())
            
            ### gonna check if the number of iteration is int
            n = int(self.ui.fi_input_iterations.text())
            
            ### final test in validating the inputs
            if n > 0:
                status_qoo = True
            else:
                qtw.QMessageBox.critical(self,"Error","Iteration must be a positive integer!")
        except:
            qtw.QMessageBox.critical(self,"Error","Inputs are invalid!")
        
        # print("Fixed point button clicked!")
        ###Confirming of the status of validation
        if status_qoo is True:
            output, isConverging = fi(gx_equation,initial_x,n)
            length = len(output)
            ###Setting max row ###
            self.ui.FI_Table.setRowCount(length)
            print(output)
            row = 0
            ###Displaying the output to the table
            for nn in range(len(output)):
                self.ui.FI_Table.setItem(row,0,qtw.QTableWidgetItem(str(row+1)))
                self.ui.FI_Table.setItem(row,1,qtw.QTableWidgetItem(str(output[row][0])))
                self.ui.FI_Table.setItem(row,2,qtw.QTableWidgetItem(str(output[row][1])))
                row+=1

            
            if isConverging < 3:
                qtw.QMessageBox.critical(self,"Error","Input another initial guess. It is not converging")
            else:
                qtw.QMessageBox.information(self,"Info","X is found!")
        else:
            qtw.QMessageBox.critical(self,"Error","Input another initial guess. It is not converging")
            pass
        
    def bisection(self):
        ###Validation First ###
        status_qoo = False
        ### Declaring symbol x
        x = Symbol('x')
        
        try:
            ### checking if a valid float ###
            input_a = float(self.ui.b_input_a.text())
            input_b =float(self.ui.b_input_b.text())
            tolerance = float(self.ui.b_input_ea.text())
            
            ### checking if a valid expression ###
            fx_equation = parse_expr(self.ui.b_input_fx.text())
            
            ###Checking if a valid integer ###
            num = int (self.ui.b_input_iterations.text())
            
            if input_a < input_b:
                
                if tolerance < 1:
                    
                    
                    if num > 0:
                        status_qoo = True
                    else:
                        qtw.QMessageBox.critical(self,"Error","Iteration must be a positive integer!")
                else:
                    qtw.QMessageBox.critical(self,"Error","Ea must be lower than 1 but greater than 0!")
            else:
                qtw.QMessageBox.critical(self,"Error","a must be lower than b")
            
        except:
            
            qtw.QMessageBox.critical(self,"Error","Inputs are invalid!")
        
        print("Bisection button clicked!")
        
        ### Confirming of the status of the validation ###
        if status_qoo is True:
            output,rooted = bb(input_a,input_b,tolerance,fx_equation,num)
            
            if rooted != "Not Found!":
                ###Displaying the output###
                self.ui.B_Table.setRowCount(len(output))
                row = 0
                
                for nn in range(len(output)):
                    self.ui.B_Table.setItem(row,0,QTableWidgetItem(str(row+1)))
                    self.ui.B_Table.setItem(row,1,QTableWidgetItem(output[row][0]))
                    self.ui.B_Table.setItem(row,2,QTableWidgetItem(output[row][1]))
                    self.ui.B_Table.setItem(row,3,QTableWidgetItem(output[row][2]))
                    self.ui.B_Table.setItem(row,4,QTableWidgetItem(output[row][3]))
                    self.ui.B_Table.setItem(row,5,QTableWidgetItem(output[row][4]))
                    row+=1
                    
                if rooted != 'x':
                    rooted = str(rooted)+" is the root!"
                    qtw.QMessageBox.information(self,"Info",rooted)
                else:
                    qtw.QMessageBox.critical(self,"Error","Input another initial a and b!")
            else:
                    qtw.QMessageBox.critical(self,"Error","Input another initial a and b!")
        else:
            qtw.QMessageBox.critical(self,"Error","Input another initial a and b!")
            

        
    def false_point(self):
        
        ##Validating the input first###
        status_qoo = False
        x = Symbol('x')
        try:
            ###Checking if valid float###
            input_a = float(self.ui.fp_input_a.text())
            input_b =float(self.ui.fp_input_b.text())
            tolerance = float(self.ui.fp_input_ea.text())
            
            ### checking if a valid expression ###
            fx_equation = parse_expr(self.ui.fp_input_fx.text())
            
            ###Checking if a valid integer ###
            num = int (self.ui.fp_input_iterations.text())
        
            if input_a < input_b:
                
                if tolerance < 1:
                    
                    
                    if num > 0:
                        status_qoo = True
                    else:
                        qtw.QMessageBox.critical(self,"Error","Iteration must be a positive integer!")
                else:
                    qtw.QMessageBox.critical(self,"Error","Ea must be lower than 1 but greater than 0!")
            else:
                qtw.QMessageBox.critical(self,"Error","a must be lower than b")
            
        except:
            qtw.QMessageBox.critical(self,"Error","Inputs are invalid!")
            
        
        print("False point button clicked!")
        
        if status_qoo == True:
            output, rooted = fp(input_a,input_b,tolerance,fx_equation,num)
            
            if rooted != "Not Found!":
                ###Display the output###
                self.ui.FP_Table.setRowCount(len(output))
                row = 0
                print(output)
                for nn in range(len(output)):
                    self.ui.FP_Table.setItem(row,0,QTableWidgetItem(str(row+1)))
                    self.ui.FP_Table.setItem(row,1,QTableWidgetItem(output[row][0]))
                    self.ui.FP_Table.setItem(row,2,QTableWidgetItem(output[row][1]))
                    self.ui.FP_Table.setItem(row,3,QTableWidgetItem(output[row][2]))
                    self.ui.FP_Table.setItem(row,4,QTableWidgetItem(output[row][3]))
                    self.ui.FP_Table.setItem(row,5,QTableWidgetItem(output[row][4]))
                    self.ui.FP_Table.setItem(row,6,QTableWidgetItem(output[row][5]))
                    self.ui.FP_Table.setItem(row,7,QTableWidgetItem(output[row][6]))
                    row+=1
                    
                if rooted != 'x':
                    rooted = str(rooted)+" is the root!"
                    qtw.QMessageBox.information(self,"Info",rooted)
                else:
                    qtw.QMessageBox.critical(self,"Error","Input another initial a and b!")
            else:
                qtw.QMessageBox.critical(self,"Error","Input another initial a and b!")
        else:
            qtw.QMessageBox.critical(self,"Error","Input another initial a and b!")

            
        pass
        
    def newton_raphson(self):
        ###Validating of input ###
        status_qoo = False
        x = Symbol('x')
        try:
            ###checking if a valid float ###
            initial_x = float(self.ui.nr_input_x.text())
            
            ###checking if a valid expression ###
            fx_equation = parse_expr(self.ui.nr_input_fx.text())
            
            ###checking if a valid integer ###
            num = int(self.ui.nr_input_iterations.text())
            
            ###derivation of f(x) ###
            gx_equation = Derivative(fx_equation,x)
            
            if num > 0:
                status_qoo = True
        except:
            qtw.QMessageBox.critical(self,"Error","Inputs are invalid!")
        
        print("Newton Raphson button clicked!")
        
        ###Confirming the status qoo ###
        if status_qoo is True:
            output, rooted = nr(initial_x,fx_equation,gx_equation,num)
            
            if rooted != "Not Found!":
                ###Display the output to the table###
                self.ui.NR_Table.setRowCount(len(output))
                row = 0
                
                for nn in range(len(output)):
                    self.ui.NR_Table.setItem(row,0,QTableWidgetItem(str(row+1)))
                    self.ui.NR_Table.setItem(row,1,QTableWidgetItem(output[row][0]))
                    self.ui.NR_Table.setItem(row,2,QTableWidgetItem(output[row][1]))
                    row +=1
                    
                if rooted != 'x':
                    rooted = str(rooted) + " is the root!"
                    qtw.QMessageBox.information(self,"Info",rooted)
                
                else:
                    qtw.QMessageBox.critical(self,"Error","Input another initial x")
            else:
                qtw.QMessageBox.critical(self,"Error","Input another initial x")
        else:
            qtw.QMessageBox.critical(self,"Error","Input another initial x!")

        
    def secant_method(self):
        ##Validating the input first###
        status_qoo = False
        x = Symbol('x')
        try:
            ###Checking if valid float###
            input_a = float(self.ui.secant_input_a.text())
            input_b =float(self.ui.secant_input_b.text())
            
            
            ### checking if a valid expression ###
            fx_equation = parse_expr(self.ui.secant_input_fx.text())
            
            ###Checking if a valid integer ###
            num = int (self.ui.secant_input_iterations.text())
        
            if input_a < input_b:
                    
                if num > 0:
                    status_qoo = True
                else:
                    qtw.QMessageBox.critical(self,"Error","Iteration must be a positive integer!")
            else:
                qtw.QMessageBox.critical(self,"Error","a must be lower than b")
            
        except:
            qtw.QMessageBox.critical(self,"Error","Inputs are invalid!")
        print("Secant Method clicked!")
        
        if status_qoo == True:
            output,rooted = sec(input_a,input_b,fx_equation,num)
            print(rooted)
            if rooted != "Not Found!":
                self.ui.Secant_Table.setRowCount(len(output))
                row = 0
                for nn in range(len(output)):
                    self.ui.Secant_Table.setItem(row,0,QTableWidgetItem(str(row+1)))
                    self.ui.Secant_Table.setItem(row,1,QTableWidgetItem(output[row][0]))
                    self.ui.Secant_Table.setItem(row,2,QTableWidgetItem(output[row][1]))
                    self.ui.Secant_Table.setItem(row,3,QTableWidgetItem(output[row][2]))
                    self.ui.Secant_Table.setItem(row,4,QTableWidgetItem(output[row][3]))
                    self.ui.Secant_Table.setItem(row,5,QTableWidgetItem(output[row][4]))
                    self.ui.Secant_Table.setItem(row,6,QTableWidgetItem(output[row][5]))
                    self.ui.Secant_Table.setItem(row,7,QTableWidgetItem(output[row][6]))
                    row+=1
                if rooted != 'x':
                    rooted = str(rooted)+" is the root!"
                    qtw.QMessageBox.information(self,"Info",rooted)
                else:
                    qtw.QMessageBox.critical(self,"Error","Input another initial a and b!")
            else:
                qtw.QMessageBox.critical(self,"Error","Input another initial a and b!")
        else:
            qtw.QMessageBox.critical(self,"Error","Input another initial a and b!")

        
        
        
if __name__ == '__main__':
    # if not sys.warnoptions:
    #     import warnings
    #     warnings.simplefilter("ignore")
    app = qtw.QApplication([])
    window = Mainwindow()
    window.show()
    app.exec_()
        