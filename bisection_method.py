from os import stat
from Equation import Expression
from sympy import *
import math
from sympy.strategies.rl import subs

def bisection_method(a,b,ea,fx,n):
    fa = fx.evalf(5,subs=dict(x=a))
    fb = fx.evalf(5,subs=dict(x=b))
    root = 'x'
    status = False
    root_status = False
    steps=0
    bisection_list = []
    if fa*fb < 0:
        status = True
        
    if status == True:
        
        while steps<n+1 and root_status == False:
            m = (a+b)/2
            if (b-m) <= ea:
                root = m
                root_status = True
            
            fm = fx.evalf(5,subs=dict(x=m))
            
            temp = [str(a),str(b),str(m),str(b-m),str(fm)]
            if fm > 0:
                b = m
            else:
                a=m
                
            bisection_list.append(temp)
            
        return bisection_list,root
    
    else:
        root = "Not Found!"
        return bisection_list,root
        
    