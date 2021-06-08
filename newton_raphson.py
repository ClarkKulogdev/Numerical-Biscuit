from Equation import Expression
from sympy import *
import math
from sympy.strategies.rl import subs

def newton_raphson_method(x0,fx,gx,n):
    root = 'x'
    status = False
    root_status = False
    steps=0
    newton_list = []
    counter = 0
    while steps<(n+1) and root_status==False:
        if counter > 3:
            root_status = True
            root = x0
        tempfx =fx.evalf(5,subs=dict(x=x0)) 
        tempgx = gx.doit().evalf(5,subs=dict(x=x0))
        x1 = x0 - (tempfx/tempgx)
        
        if round(x0,5) == round(x1,5):
            counter += 1
        temp = [str(round(x0,5)),str(round(x1,5))]
        newton_list.append(temp)
        x0 = x1
        steps+=1
        
    if counter > 3:
        root_status = True
        
    if root_status == True:
        
        return newton_list, root
    else:
        root = "Not Found!"
        return newton_list,root
        
        