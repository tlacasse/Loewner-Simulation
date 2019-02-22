import numpy as np
import numexpr
from Equation import Expression

# force to upper half-plane
def _zflip(z):
    return z if z.imag >= 0 else -z

zflip = np.vectorize(_zflip)

def fix_equation_input(eq):
    result = ""
    for i in range(len(eq)):
        if (i > 0 and eq[i].isalpha() and eq[i-1].isnumeric()):
            result += '*'
        result += eq[i]
    return result

class LESimulation:
    
    def __init__(self, driving_function, time_upper_bound, sample_count):
        self.driving_function_text = fix_equation_input(driving_function)
        self.driving_function = Expression(self.driving_function_text, ['t'])
        self.time_upper_bound = time_upper_bound
        self.sample_count = sample_count
        
        self.time_step_part = time_upper_bound / (self.sample_count - 1)
        self.time_step_part = -4 * self.time_step_part  
        
        self.setup_samples()
        
    def setup_samples(self):
        self.time_domain = np.linspace(0, self.time_upper_bound, self.sample_count)
        self.time_domain = self.time_domain[::-1]
        self.samples = np.empty(self.sample_count, dtype='double')
        self.samples[:] = self.driving_function(self.time_domain[:])
        self.hull = self.samples.astype(dtype='complex128')
    
    # upward LE conformal map for constant driving function
    # time_step = -4t
    def conformal_map(self, z, c, time_step):
        return zflip(numexpr.evaluate('sqrt(((z - c) ** 2) + time_step)')) + c

    def compute_hull(self):
        for i in range(1, len(self.hull)):
            self.hull[:i] = self.conformal_map(self.hull[:i], self.samples[i-1], self.time_step_part)
        return self.hull
