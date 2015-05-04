# Exercise 3.1
# Davis Sandefur
# Completed on 3/5/2015

from pylab import plot,show, xlabel, ylabel
from numpy import loadtxt

data = loadtxt("sunspots.txt", float)

x = data[:,0]
y = data[:,1]
plot(x,y)
xlabel("Month number (Start: January 1749)")
ylabel("Number of sunspots")

show()
