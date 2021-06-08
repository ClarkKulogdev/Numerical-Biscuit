from Equation import Expression
from sympy import *
import math
from sympy.strategies.rl import subs

def secant_method(a,b,fx,n):
    fa = fx.evalf(5,subs=dict(x=a))
    fb = fx.evalf(5,subs=dict(x=b))
    root = 'x'
    status = False
    root_status = False
    num= 0
    cold = 0
    secant_list = []
    if fa*fb < 0:
        status = True
        
    if status == True:
        
        while num< (n+1) and root_status==False:
            #Step 2 #
            tempa = a
            tempb = b
            ##Step2##
            fa = fx.evalf(5,subs=dict(x=a))
            fb = fx.evalf(5,subs=dict(x=b))
            cnew = b - (fb*(b-a))/(fb-fa)
            fc = fx.evalf(5,subs=dict(x=cold))
            ##Step3##
            ea = ((cnew-cold)/cnew)*100
            ##Step4##
            if ea == 0:
                root = cnew
                temp = [str(tempa), str(tempb),str(fa), str(fb),str(cnew),str(fc),str(ea)]
                secant_list.append(temp)
                root_status = True
            else:
                num +=1
                a = b
                b = cnew
                cold = cnew
                temp = [str(tempa), str(tempb),str(fa), str(fb),str(cnew),str(fc),str(ea)]
                secant_list.append(temp)
                
        return secant_list,root
    else:
        root = "Not Found!"
        return secant_list,root