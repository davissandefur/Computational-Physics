# Problem 2.a
# Completed by Davis Sandefur
# 5.5.2015

from math import pi
from numpy import linspace, sin, cos
from pylab import plot, show

ypoints = [(2*sin(theta) - sin(2*theta)) for theta in linspace(0,2*pi,1000)]
xpoints = [(2*cos(theta) - sin(2*theta)) for theta in linspace(0,2*pi,1000)]

plot(xpoints,ypoints)
show()
