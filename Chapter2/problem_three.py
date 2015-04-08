# Davis Sandefur
# Completed 7 April, 2015

from math import sqrt, atan, degrees

def polar(x,y):
	""" This function takes the Cartesian coordinates (x,y) and returns the polar coodinates associated with them, with theta being in degrees."""
	
	radius = sqrt(x**2 + y**2)
	
	# Take care of when x is 0
	if x == 0 and y>0:
		theta = 90;
	elif x == 0 and y <0:
		teta = 270;
	else:
		theta = degrees(atan(y/x))
	
	return (radius, theta)

if __name__ == '__main__':
	# Test it with known cases
	print (polar(0,1))
	print (polar(1,0))
	print (polar(1,1))
	print (polar(1,sqrt(3)))
