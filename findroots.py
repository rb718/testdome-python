# Implement the function find_roots to find the roots of the quadratic equation: ax2 + bx + c = 0. The function should return a tuple containing roots in any order. If the equation has only one solution, the function should return that solution as both elements of the tuple. The equation will always have at least one solution.

# The roots of the quadratic equation can be found with the following formula: A quadratic equation.

# For example, find_roots(2, 10, 8) should return (-1, -4) or (-4, -1) as the roots of the equation 2x2 + 10x + 8 = 0 are -1 and -4.

import numpy as np

def find_roots(a, b, c):
    input = [a, b, c]
    return tuple(np.roots(input))

print(find_roots(2, 10, 8));

################################################

import math

def find_roots(a, b, c):
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = round(((-b + math.sqrt(D)) / (2 * a)), 2)
        x2 = round(((-b - math.sqrt(D)) / (2 * a)), 2)
        return (x1, x2)
    elif D == 0:
        x1 = x2 = -b / 2 * a
        return x1
    else:
        return 'The equation has no solution'

print(find_roots(2, 10, 8));