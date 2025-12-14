import numpy as np
import math
import matplotlib.pyplot as plt

usr_angle=float(input("Enter Angle Degrees:"))
usr_velocity=float(input("Enter Velocity m/s:"))

time_flight=(2*usr_velocity*math.sin((usr_angle*math.pi)/180))/(9.80)

t=np.linspace(0,time_flight,500)

print(time_flight)



y= (t*usr_velocity*math.sin((usr_angle*math.pi)/180))-(0.5*9.80*(t**2))
x= t*usr_velocity*math.cos((usr_angle*math.pi)/180)
   


usr_t=float(input("Enter time:"))
x_demanded=usr_t*usr_velocity*math.cos((usr_angle*math.pi)/180)
y_demanded=(usr_t*usr_velocity*math.sin((usr_angle*math.pi)/180))-(0.5*9.80*(usr_t**2))




plt.plot(x,y)
plt.plot(x_demanded,y_demanded,marker="o")
plt.show()
