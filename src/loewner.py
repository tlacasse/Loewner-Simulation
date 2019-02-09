# -*- coding: utf-8 -*-
import numpy as np
import numexpr
from Equation import Expression

# force to upper half-plane
def imflip(z):
    return z if z.imag >= 0 else -z

# use first letter found as the variable for the expression
def create_driving_function(equation_string):
    var = 't'
    for c in equation_string:
        code = ord(c)
        # exlcude 'e' as it's Euler's constant
        if (code >= ord('a') and code <= ord('z') and not code == ord('e')):
            var = c
            break
    return Expression(equation_string, [var])

class LESimulation:
    
    def __init__(self, driving_function, time_upper_bound, sample_count):
        self.driving_function = create_driving_function(driving_function)
        self.time_upper_bound = time_upper_bound
        self.mappings_count = sample_count - 1
        self.time_step_part = time_upper_bound / self.mappings_count
        self.time_step_part = -4 * self.time_step_part
        self.sample_count = sample_count
        
        self.samples = np.empty(sample_count, dtype='complex128')
        for i in range(sample_count):
            self.samples[i] = self.xi(i) 
            
        self.hull = self.samples.copy()

    # reverse driving function at sample i
    def xi(self, i):
        frac_of_time = 1 - (i / self.mappings_count)
        return self.driving_function(self.time_upper_bound * frac_of_time)
    
    # upward LE conformal map for constant driving function
    # time_step = -4t
    def conformal_map(self, z, c, time_step):
        return numexpr.evaluate('sqrt(((z - c) ** 2) + time_step) + c')

    def compute_hull(self):
        for i in range(1, len(self.hull)):
            self.hull[:i] = self.conformal_map(self.hull[:i], self.samples[i-1], self.time_step_part)
        return self.hull
