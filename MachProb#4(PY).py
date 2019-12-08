import math as math
import numpy as np
import matplotlib.pyplot as plt
print("---This is a projectile motion graph generator--- \n")
print("---Everything is set in KGM units---")
print("")
h1 = float(input('Please input the initial height(m): '))
print("")
v1 = float(input('Please input the initial velocity(m/s): '))
print("")
angle = float(input('Please input the angle in degrees: '))
print("")
ax = float(input('Please input acceleration in the x direction(m/s^2): '))
print("")
ay1 = float(input('Please input acceleration in the y direction(m/s^2): '))
#All the input values given by the user
print("")
ay = -ay1
#Will make ay1(acceleration in the y direction) negative, so it results into a freefall
print("")
while ay == 0 or ay > 0:
    #if the set ay is lower than zero, the user will have to re-input its value.
    print('Vertical acceleration will not result in freefall.\n Please input a value higher than 0\n ')
    ay1 = float(input("Please re-input the acceleration in the y direction: "))
    ay = -ay1


while angle > 90:
    #if the set angle is higher than 90, the user will have to re-input its value.
    print("Maximum angle is set at 90 degrees.\n Please do not exceed 90 degrees\n")
    angle = float(input("Please re-input the angle that fit the parameters: "))
angle = math.radians(angle)
#will convert radians to degrees
v1x = v1*math.cos(angle)
v1y = v1*math.sin(angle)
#will get the angle of the angle and 
rt = [ay/2, v1y, h1]
tm = np.roots(rt)
#Will take the roots
tm = max(tm)

d = np.arange(0,tm,0.1)
y = np.zeros((len(d),1))
x = np.zeros((len(d),1))

t = 0.1
y[0,0] = h1

n = np.arange(0,len(d),1)
for i in n:
    xt = (ax*(t**2))/2 + v1x*t
    yt = (ay*(t**2))/2 + v1y*t + h1
    x[i,0] = xt
    y[i,0] = yt
    t=t+0.1
#Datapoints to be plotted
plt.plot(x,y)
plt.autoscale(enable = True, axis = 'both', tight = True)
plt.xlabel("Distance(Meters)")
plt.ylabel("Height(Meters)")
plt.grid()
