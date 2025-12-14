import numpy as np
import matplotlib.pyplot as plt
k=10
w=20

x=np.linspace(-1000000,10000000,500)

t=np.linspace(-100,100,500)

y=0.001*np.cos((k*x)-(w*t))

plt.plot(x,y)
plt.show()
