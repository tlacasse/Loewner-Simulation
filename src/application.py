import tkinter as tk
import time
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from loewner import LESimulation

class Application(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.setup()

    def setup(self):
        self.master.title('Loewner Simulation')
        self.master.geometry("1024x640")
        
        self.label_entry_df = tk.Label(self, text = 'Driving Function (t): ')
        self.label_entry_df.grid(row = 1, column = 1, padx = 10, pady = 10)
        self.entry_df = tk.Entry(self, exportselection = 0)
        self.entry_df.insert(0, 't')
        self.entry_df.grid(row = 1, column = 2)
        
        self.label_entry_time = tk.Label(self, text = 'Time Bound: ')
        self.label_entry_time.grid(row = 2, column = 1, padx = 10, pady = 10)
        self.entry_time = tk.Entry(self, exportselection = 0)
        self.entry_time.insert(0, '20')
        self.entry_time.grid(row = 2, column = 2)
        
        self.label_entry_samples = tk.Label(self, text = '# Samples: ')
        self.label_entry_samples.grid(row = 3, column = 1, padx = 10, pady = 10)
        self.entry_samples = tk.Entry(self, exportselection = 0)
        self.entry_samples.insert(0, '1000')
        self.entry_samples.grid(row = 3, column = 2)
        
        self.button_run = tk.Button(self)
        self.button_run['text'] = 'Run'
        self.button_run['command'] = self.run_simulation
        self.button_run.grid(row = 4, column = 2, ipadx = 20)
        
        self.label_time = tk.Label(self)
        self.label_time.grid(row = 4, column = 3)
        
        self.figure_df = Figure(figsize=(5, 4), dpi = 95)
        self.canvas_df = FigureCanvasTkAgg(self.figure_df, master = self)
        self.canvas_df.draw()
        self.canvas_df.get_tk_widget().grid(row = 5, column = 1, columnspan = 3, 
                            padx = 10, pady = 10)
        
        self.figure_hull = Figure(figsize=(5, 4), dpi = 95)
        self.canvas_hull = FigureCanvasTkAgg(self.figure_hull, master = self)
        self.canvas_hull.draw()
        self.canvas_hull.get_tk_widget().grid(row = 5, column = 4,
                            padx = 10, pady = 10)

    def run_simulation(self):
        sim = LESimulation(self.entry_df.get(), 
                           int(self.entry_time.get()), 
                           int(self.entry_samples.get()))
        start = time.time()
        hull = sim.compute_hull()
        stop = time.time()
        for i in hull:
            print(i)
        
        self.label_time['text'] = 'Computation Time: ' + str(stop - start) + 's'
        
        self.figure_df.clf()
        self.figure_df.add_subplot(111).plot(sim.time_domain, sim.samples)
        self.canvas_df.draw()
        
        self.figure_hull.clf()
        self.figure_hull.add_subplot(111).plot(hull.real, hull.imag)
        self.canvas_hull.draw()
