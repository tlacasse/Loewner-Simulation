import tkinter as tk

class InputFrame(tk.Frame):
    
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.setup() 
        
    def setup(self):
        self.label_entry_df, self.entry_df = (
            self.create_text_input('Driving Function (t):', 't', 0))
        
        self.label_entry_time, self.entry_time = (
            self.create_text_input('Time Bound:', '20', 1))
        
        self.label_entry_samples, self.entry_samples = (
            self.create_text_input('# Samples:', '1000', 2))
        
    def create_text_input(self, prompt, default, i):
        newlabel = tk.Label(self, text = prompt)
        newinput = tk.Entry(self, exportselection = 0)
        newinput.insert(0, default)
        
        newlabel.grid( row = i, column = 0, padx = 10, pady = 10 )
        newinput.grid( row = i, column = 1 )
        
        return newlabel, newinput
    
    def update_from_sim(self, sim):
        self.entry_df.delete(0, tk.END)
        self.entry_df.insert(0, sim.driving_function)
        
    def get_df(self):
        return self.entry_df.get()
    
    def get_time_bound(self):
        return int(self.entry_time.get())
    
    def get_samples(self):
        return int(self.entry_samples.get())

