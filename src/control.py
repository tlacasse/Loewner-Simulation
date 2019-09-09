import tkinter as tk

from ui.frames.error.errormessage import ErrorMessageFrame

import time

class Control:
    
    def __init__(self, app):
        self.app = app
        self.sim = None

    def execute(self, func, timeit=True):
        try:
            start = time.time()
            func()
            stop = time.time()
            if timeit:
                self.update_message('Computation Time: ' + str(stop - start) + 's')
        except Exception as e:
            message = repr(e)
            self.display_error_message(message)
            
    def update_message(self, text):
        def func():
            self.app('run_message').update(text)
        self.execute(func, timeit=False)
        
    def display_error_message(self, text):
        def func():
            popup = tk.Toplevel()
            popup.wm_title('Error')
            frame = ErrorMessageFrame(popup, self, text)
            frame.grid()
        self.execute(func, timeit=False)
        
    def run_simulation(self):
        def func():
            sim = self.app('input').build_sim()
            self.sim = sim
            sim.compute_hull()
            self.app('graph_df').update(sim.time_domain, sim.samples)
            self.app('graph_hull').update(sim.hull.real, sim.hull.imag)
        self.execute(func)
        
