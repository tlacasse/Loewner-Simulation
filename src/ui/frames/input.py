from ui.frames.blank import BlankFrame

import tkinter as tk
from loewner.sim import LESimulation

class InputFrame(BlankFrame):
    
    def __init__(self, master=None, control=None):
        super().__init__(master, control)
        
    def setup(self):
       self.entry_df = self.create_text_input('Driving Function (t):', 't', 0)
       self.entry_time = self.create_text_input('Time Bound:', '20', 1)
       self.entry_samples = self.create_text_input('# Samples:', '1000', 2)
    
    def create_text_input(self, prompt, default, i):
        newlabel = tk.Label(self, text=prompt)
        newinput = tk.Entry(self, exportselection=0)
        newinput.insert(0, default)
        
        newlabel.grid(row=i, column=0, padx=10, pady=10)
        newinput.grid(row=i, column=1)  
        return newinput
    
    def get_driving_function(self):
        return self.entry_df.get()
    
    def get_time_bound(self):
        return int(self.entry_time.get())
    
    def get_sample_count(self):
        return int(self.entry_samples.get())
    
    def build_sim(self):
        sim = LESimulation()
        sim.init_equation(self.get_driving_function(), 
                          self.get_time_bound(), 
                          self.get_sample_count())
        
        self.entry_df.delete(0, tk.END)
        self.entry_df.insert(0, sim.driving_function)
        return sim
