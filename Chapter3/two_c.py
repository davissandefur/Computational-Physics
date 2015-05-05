# Problem 2.c
# Completed by Davis Sandefur
# 5.5.2015

from numpy import sin, cos, linspace
from math import pi, e
from pylab import show, plot

theta = linspace(0,24*pi,100000)
r = e**(cos(theta)) - 2*cos(4*theta) + sin(theta/12)**5
x = r*cos(theta)
y = r*sin(theta)

plot(x,y)
show()
