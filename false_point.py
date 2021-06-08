from Equation import Expression
from sympy import *
import math
from sympy.strategies.rl import subs

def false_point_method(a,b,ea,fx,n):
    fa = fx.evalf(5,subs=dict(x=a))
    fb = fx.evalf(5,subs=dict(x=b))
    root = 'x'
    status = False
    root_status = False
    num=0
    false_point_list = []
    if fa*fb < 0:
        status = True
    
    if status == True:
        
        while num< (n+1) and root_status==False:
            #Step 2 #
            tempa = a
            tempb = b
            fa = fx.evalf(5,subs=dict(x=a))
            fb = fx.evalf(5,subs=dict(x=b))
            c = b - (fb*(a-b))/(fa-fb)
            # Step 3 #
            fc = fx.evalf(5,subs=dict(x=c))
            if abs(fa) + abs(fc) == abs(fa + fc):
                step=abs(a-c)
                a = c
            elif abs(fb) + abs(fc) == abs(fb + fc): 
                step = abs(b-c)
                b = c
            
            ### Step 4 ###
            if step <= ea and step>=0:
                root_status=True
                root = c
                templist = [str(tempa),str(tempb),str(fa),str(fb),str(c),str(fc),str(step)]
                false_point_list.append(templist)
                
            else:
                num+=1
                templist = [str(tempa),str(tempb),str(fa),str(fb),str(c),str(fc),str(step)]
                false_point_list.append(templist)
                
        return false_point_list, root
    
    else:
        root = "Not Found!"
        return false_point_list,root

                
            
                
            
            
            
