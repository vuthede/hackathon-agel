import random
import math
'''
Contains all global variables specific to simulation
'''
# Defines range for coordinates when dustbins are randomly scattered
numGenerations = 100
populationSize = 100
mutationRate = 0.02
tournamentSize = 3
elitism = True

hash_table_route = {}


def random_range(n, total):
    """Return a randomly chosen list of n positive integers summing to total.
    Each such list is equally likely to occur."""

    dividers = sorted(random.sample(range(1, total), n - 1))
    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]

# Randomly distribute number of dustbins to subroutes
# Maximum and minimum values are maintained to reach optimal result
def route_lengths(numNodes, numTrucks):
    upper = (numNodes + numTrucks - 1)
    fa = upper/numTrucks*1.6 # max route length
    fb = upper/numTrucks*0.6 # min route length
    a = random_range(numTrucks, upper)
    while 1:
        if all( i < fa and i > fb  for i in a):
                break
        else:
                a = random_range(numTrucks, upper)
    return a




#print(route_lengths())



