import time

class Control:
    
    def __init__(self, app):
        self.app = app
        self.sim = None

    def execute(self, func):
        try:
            start = time.time()
            func()
            stop = time.time()
            self.update_message('Computation Time: ' + str(stop - start) + 's')
        except Exception as e:
            message = str(e)
            #message = message[(message.rfind(')')+1):]
            self.update_message(message) #todo: improve this
            
    def run_simulation(self):
        sim = self.app('input').build_sim()
        self.sim = sim
        sim.compute_hull()
        self.app('graph_df').update(sim.time_domain, sim.samples)
        self.app('graph_hull').update(sim.hull.real, sim.hull.imag)
        
    def update_message(self, text):
        self.app('run_message').update(text)
