import numpy as np
import math
import matplotlib.pyplot as plt

usr_angle=float(input("Enter Angle Degrees:"))
usr_velocity=float(input("Enter Velocity m/s:"))

time_flight=(2*usr_velocity*math.sin((usr_angle*math.pi)/180))/(9.80)

t=np.linspace(0,time_flight,500)

print(time_flight)

y=[]
x=[]

for i in t:
    y_t= (i*usr_velocity*math.sin((usr_angle*math.pi)/180))-(0.5*9.80*(i**2))
    x_t= i*usr_velocity*math.cos((usr_angle*math.pi)/180)
    x.append(x_t)
    y.append(y_t)


usr_t=float(input("Enter time:"))
x_demanded=usr_t*usr_velocity*math.cos((usr_angle*math.pi)/180)
y_demanded=(usr_t*usr_velocity*math.sin((usr_angle*math.pi)/180))-(0.5*9.80*(usr_t**2))




plt.plot(x,y)
plt.plot(x_demanded,y_demanded,marker="o")
plt.show()