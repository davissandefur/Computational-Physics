# Davis Sandefur
# Completed on 21 April, 2015

from math import sqrt, pow


def probability(m, E, V):
    h_bar = 1.05  # mmkg/s

    k1 = sqrt(2*m*E)/h_bar
    k2 = sqrt(2*m*(E-V))/h_bar

    T = (4*k1*k2)/(k1+k2)**2  # Probability of transmission
    R = ((k1-k2)/(k1+k2))**2  # Probability of reflection

    return T, R

if __name__ == '__main__':

    Transmission, reflection = probability(9.11*pow(10, 11), 10, 9)
    print(Transmission, reflection)