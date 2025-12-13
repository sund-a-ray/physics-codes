import math
import matplotlib.pyplot as plt
import numpy as np


x_input=np.linspace(-1,1,500)

p_0=[]
p_1=[]
p_2=[]
p_3=[]
p_4=[]


for i in x_input:
    y0=1
    p_0.append(y0)

    y1=i
    p_1.append(y1)

    y2=0.5*(3*((i)**2)-1)
    p_2.append(y2)

    y3=0.5*((5*(i**3))-(3*i))
    p_3.append(y3)

    y4=0.125*((35*(i**4))-(30*(i**2))+(3))
    p_4.append(y4)


plt.plot(x_input,p_0)
plt.plot(x_input,p_1)
plt.plot(x_input,p_2)
plt.plot(x_input,p_3)
plt.plot(x_input,p_4)

plt.show()
    
