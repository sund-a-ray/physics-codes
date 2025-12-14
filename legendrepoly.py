import math
import matplotlib.pyplot as plt
import numpy as np


x_input=np.linspace(-1,1,500)

p =[]

usr_want= int(input("Enter legendre poly index(0-4):"))



if usr_want<5:
 for i in x_input:
   if usr_want==0: 
    y0=1
    p.append(y0)

   elif usr_want==1: 
    y1=i
    p.append(y1)

   elif usr_want==2:
    y2=0.5*(3*((i)**2)-1)
    p.append(y2)

   elif usr_want==3:
    y3=0.5*((5*(i**3))-(3*i))
    p.append(y3)

   elif usr_want==4:
    y4=0.125*((35*(i**4))-(30*(i**2))+(3))
    p.append(y4)

else:
    print("invalid input") 

if p:
 plt.plot(x_input,p)

 plt.show()
    
