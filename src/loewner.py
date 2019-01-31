# -*- coding: utf-8 -*-
import cmath
import numpy as np
from Equation import Expression

# force to upper half-plane
def imflip(z):
    return z if z.imag >= 0 else -z

class LESimulation:
    
    def __init__(self, driving_function, time_upper_bound, sample_count):
        self.driving_function = Expression(driving_function, ["x"])
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
    def conformal_map(self, z, c):
        sq = (z - c) ** 2
        return cmath.sqrt(sq + self.time_step_part) + c
    
    def compute_hull(self):
        for z in range(len(self.hull)):
            for c in range(z, self.mappings_count):
                self.hull[z] = self.conformal_map(self.hull[z], self.samples[c])
        return self.hull
