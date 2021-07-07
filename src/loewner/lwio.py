from loewner.sim import LESimulation
import numpy as np
import numexpr

def clean_complex(z):
    if (hasattr(z, 'real')):
        s = str(z).replace('j','i')
        if (s[0] == '('):
            s = s[1:-1]
        if (z.real == 0):
            s = '0.0+' + s
        return s
    else:
        return str(z)

def read_complex(zstr):
    # complex() cannot have extra spaces
    return complex(zstr.replace(' ', '').replace('i', 'j'))

def export_sim(sim, file_name, export_info):
    headers = []
    maps = []
    if (export_info['samples']):
        headers.append('lambda(t)')
        maps.append(lambda sim, i: sim.samples[i])
    if (export_info['hull']):
        headers.append('hull')
        maps.append(lambda sim, i: clean_complex(sim.hull[i]))
    if (export_info['xy']):
        headers.append('hull-x')
        headers.append('hull-y')
        maps.append(lambda sim, i: sim.hull[i].real)
        maps.append(lambda sim, i: sim.hull[i].imag)
    
    with open(file_name, 'w') as file:
        fields = ['t']
        for header in headers:
            fields.append(header)
        file.write(','.join(fields) + '\n')
        
        for i in range(sim.sample_count):
            values = [str(sim.time_domain[i])]
            for mapper in maps:
                values.append(str(mapper(sim, i)))
            file.write(','.join(values) + '\n')
            
class ImportFile:
    
    def __init__(self, file_name):
        with open(file_name, 'r') as file:
            self.lines = file.readlines()
            
        try:
            read_complex(self.lines[0].split(',')[0])
            self.has_header = False
        except ValueError:
            self.has_header = True
            
        if (self.has_header):
            self.headers = self.lines[0].split(',')
            self.lines = self.lines[1:]
        else:
            self.headers = None
            
        if (self.lines[-1].strip() == ''):
            self.lines = self.lines[:-1]
            
        self.columns = len(self.lines[1].split(','))
        self.rows = len(self.lines)
        
        self.column_lambda = np.empty(self.rows, dtype='double')
        if (self.includes_time_values()):
            self.column_time = np.empty(self.rows, dtype='double')
        else:
            self.column_time = None
        
        i = 0
        for l in self.lines:
            if (self.includes_time_values):
                values = l.split(',')
                self.column_time[i] = float(values[0].strip())
                self.column_lambda[i] = float(values[1].strip())
            else:
                self.column_lambda[i] = float(l)
            i += 1
            
    def includes_time_values(self):
        return self.columns > 1
    
    def create_sim(self, time_bound = 0.0, trans_func = 'x'):
        if (not self.includes_time_values()):
           self.column_time = np.linspace(0, time_bound, self.rows)
           
        # sort both columns
        combined = list(zip(self.column_time, self.column_lambda))
        combined.sort(key=(lambda x: x[0]), reverse=True)
        column_time = np.array([x[0] for x in combined])
        column_lambda = np.array([x[1] for x in combined])
        
        x = self.column_lambda ;x=x
        column_lambda = numexpr.evaluate(trans_func)
        
        sim = LESimulation()
        sim.init_points(column_time, column_lambda)
        return sim
