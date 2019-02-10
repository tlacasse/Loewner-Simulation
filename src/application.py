import tkinter as tk
from loewner import LESimulation
import time

class Application(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.setup()

    def setup(self):
        self.master.title('Loewner Simulation')
        self.master.geometry("400x300")
        
        self.label_text_df = tk.Label(self, text='Driving Function (t): ')
        self.label_text_df.grid(row=1, column=1)
        
        self.entry_df = tk.Entry(self, exportselection=0)
        self.entry_df.grid(row=1,column=2)
        
        self.button_run = tk.Button(self)
        self.button_run['text'] = 'Run'
        self.button_run['command'] = self.run_simulation
        self.button_run.grid(row=2,column=2)
        
        self.label_time = tk.Label(self)
        self.label_time.grid(row=3,column=2)

    def run_simulation(self):
        sim = LESimulation(self.entry_df.get(), 20, 1000)
        start = time.time()
        sim.compute_hull()
        stop = time.time()
        self.label_time['text'] = 'Computation Time: ' + str(stop - start) + 's'
