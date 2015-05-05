# Problem 2.b
# Completed by Davis Sandefur
# 5.5.2015

from numpy import sin, cos, linspace
from math import pi
from pylab import plot, show

r = [theta**2 for theta in linspace(0,10*pi,10000)]
theta = linspace(0,10*pi,10000)

x = r*cos(theta)
y = r*sin(theta)

plot(x,y)
show()
