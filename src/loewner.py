import numpy as np
import numexpr
from brownian import brownian

# force to upper half-plane
def _zflip(z):
    return z if z.imag >= 0 else -z

zflip = np.vectorize(_zflip)

def fix_equation_input(eq):
    result = ''
    for i in range(len(eq)):
        if (i > 0 and eq[i].isalpha() and eq[i-1].isnumeric()):
            result += '*'
        result += eq[i]
    return result

class LESimulation:
    
    def __init__(self):
        self.initialized = False
        self.init_type = ''
        
    def init_equation(self, driving_function, time_upper_bound, sample_count):
        self.driving_function = fix_equation_input(driving_function)
        self.time_upper_bound = time_upper_bound
        self.sample_count = sample_count
        
        self.time_step_part = np.empty(self.sample_count - 1, dtype='double')
        time_step_part = time_upper_bound / (self.sample_count - 1)
        time_step_part = -4 * time_step_part
        self.time_step_part[:] = time_step_part  
        
        self.time_domain = np.linspace(0, self.time_upper_bound, self.sample_count)
        self.time_domain = self.time_domain[::-1]
        self.samples = np.empty(self.sample_count, dtype='double')
        self.setup_samples_from_equation()
        
        self.hull = self.samples.astype(dtype='complex128')
        self.initialized = True
        self.init_type = 'equation'
        
        print(self.time_step_part)
        
    def init_points(self, time_domain, samples):
        self.driving_function = ''
        
        self.time_upper_bound = max(time_domain)
        self.sample_count = len(samples)
        
        self.time_domain = np.array(time_domain, dtype='double')
        self.samples = np.array(samples, dtype='double')
        
        self.time_step_part = np.empty(self.sample_count - 1, dtype='double')
        for i in range(self.sample_count - 1):
            self.time_step_part[i] = -4 * abs(
                    self.time_domain[i + 1] - self.time_domain[i]) # need to fix
        
        self.hull = self.samples.astype(dtype='complex128')
        self.initialized = True
        self.init_type = 'file'
        
    def setup_samples_from_equation(self):
        try:
            # throws an exception if not found
            if (self.driving_function.index('Bt')+1):
                x0 = 0.0
                n = self.sample_count - 1
                dt = self.time_upper_bound / n
                delta = 1
                
                Bt = brownian(x0, n, dt, delta)[::-1]
                Bt = np.resize(Bt, n + 1)
                Bt[-1] = x0
                self.Bt = Bt
        except:
            pass
        
        t = self.time_domain ;t=t
        # "+(0*t)" to ensure the correct number of samples (for constant functions)
        eq = '(' + self.driving_function + ')+(0*t)'
        self.samples = numexpr.evaluate(eq)
    
    # upward LE conformal map for constant driving function
    # time_step = -4t
    def conformal_map(self, z, c, time_step):
        return zflip(numexpr.evaluate('sqrt(((z - c) ** 2) + time_step)')) + c

    def compute_hull(self):
        self.hull = self.samples.astype(dtype='complex128')
        for i in range(1, len(self.hull)):
            self.hull[:i] = self.conformal_map(self.hull[:i], self.samples[i-1], self.time_step_part[i-1])
        return self.hull
