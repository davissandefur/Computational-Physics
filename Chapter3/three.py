# Solution to problem 3 of Computational Physics
# Completed by Davis Sandefur
# 10.5.15

from pylab import imshow, show
from numpy import loadtxt

data = loadtxt("stm.txt",float)
imshow(data, origin="lower", extent=[320,380,220,280])
show()
