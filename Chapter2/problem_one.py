# Davis Sandefur
# Completed on April 6, 2015

from math import sqrt

def tower():
	""" This function requests a height from the user and inputs the time it takes the ball to reach the ground from that height. """
	height = float(input("Enter the height of the tower: "))
	gravity = 9.8  # g, rounded
	
	return  sqrt(2*height/gravity)

if __name__ == '__main__':
	print(tower())

# Answer for 100m high tower: 4.52 seconds
