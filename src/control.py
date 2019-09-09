import tkinter as tk

from ui.frames.error.errormessage import ErrorMessageFrame
from ui.container import ExportPopupFrameContainer

import time
import loewner.lwio as lwio

class Control:
    
    def __init__(self, app):
        self.app = app
        self.sim = None
        self.popup_export = None

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
        
    def display_export_popup(self):
        def func():
            popup = tk.Toplevel()
            popup.wm_title('Export Simulation')
            frame = tk.Frame(popup)
            frame.setup = (lambda: True)
            self.popup_export = ExportPopupFrameContainer()
            self.popup_export.setup(frame, self)
        self.execute(func, timeit=False)
        
    def run_simulation(self):
        def func():
            sim = self.app('input').build_sim()
            self.sim = sim
            sim.compute_hull()
            self.app('graph_df').update(sim.time_domain, sim.samples)
            self.app('graph_hull').update(sim.hull.real, sim.hull.imag)
        self.execute(func)
        
    def export_simulation(self):
        def destroy_popup():
            self.popup_export.root.master.destroy()
            self.popup_export = None
        def func():
            pass
            what = self.popup_export('options').get_what_to_export()
            path = self.popup_export('path').get_export_path()
            lwio.export_sim(self.sim, path, what)
            destroy_popup()
        self.execute(func)
