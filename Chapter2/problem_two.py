# Davis Sandefur
# Completed 6 April, 2015

from math import pi, pow

def altitude():
	""" This program asks a user for the satellite orbital period and returns the altitude the satellite must be at to have that period."""
	
	# Define initial constants
	G = 6.67 * 10**-11
	M = 5.97 * 10**24
	R = 6731000

	period = float(input("Please input the orbital period of the satellite in minutes: ")) * 60  # Convert input to seconds for G 
	
	numerator = G * M * (period)**2
	denom = 4 * pi**2
	fraction = (numerator/denom) ** (1/3)
	altitude = fraction - R

	print("The required altitude is ", altitude, "meters")

if __name__ == '__main__':
	altitude()

# Part A: No computational answer required
# Part B: See above
# Part C: Geosynchronous (given 24 hours): 35,500 km
# Part D: No computational answer; less than 100 meters.

