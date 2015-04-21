# Davis Sandefur
# Completed 14 April, 2015

from math import sqrt

def relativity(x, v):
	""" This function takes a distance, x (in light years), and a velocity, v, (as a fraction of the speed of light) and calculates the time on Earth for the trip and the time as experienced by the people in the spacecraft."""

	time_earth = x/v
	gamma = (sqrt(1-(v**2/1)))
	time_spaceship = time_earth * gamma
	
	return time_earth, time_spaceship

# Answer: 1.42

if __name__ == '__main__':
	earth, spaceship = relativity(10,.99)
	print(earth,spaceship)	
