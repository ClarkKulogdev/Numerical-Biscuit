from Equation import Expression
from sympy import *
import math

from sympy.strategies.rl import subs

def fixed_point_method(gx,initial_x0,n):
    x = Symbol('x')
    steps=0
    dual_list = []
    counter=0
    status = True
    
    ###test print ###
    # print(gx)
    # print(initial_x0)
    # print(n)
    while(status):
        if counter > 3:
            status = False
        
        if steps == n:
            status= False
        
        x1 = gx.evalf(4,subs=dict(x=initial_x0))
        temp = [initial_x0, x1]
        dual_list.append(temp)
        ###checking to the 3 decimal places
        if float("{:.3f}".format(initial_x0)) == float("{:.3f}".format(x1)):
            counter += 1
        initial_x0 = x1
        steps+=1
        

        
    ###Testing###    
    # for num in dual_list:
    #     print(num)
    
    ### Return the list to the main program for deployment
    return dual_list, counter