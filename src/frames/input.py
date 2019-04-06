import tkinter as tk
import tkinter.filedialog as filedialog

import lwio

class InputFrame(tk.Frame):
    
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.mode_elements = {}
        self.input_file = None
        self.setup()
        
    def setup(self):
        self.label_entry_df, self.entry_df = (
            self.create_text_input('Driving Function (t):', 't'))
        
        self.label_entry_time, self.entry_time = (
            self.create_text_input('Time Bound:', '20'))
        
        self.label_entry_samples, self.entry_samples = (
            self.create_text_input('# Samples:', '1000'))
                                                           
        self.mode_elements['equation'] = [self.label_entry_df, self.entry_df, 
                          self.label_entry_time, self.entry_time, 
                          self.label_entry_samples, self.entry_samples]
        
        self.button_getpath = tk.Button(self)
        self.button_getpath['text'] = 'Choose Import Path'
        self.button_getpath['command'] = self.pick_import_path
        
        self.label_import_path = tk.Label(self, text = 'TEST')
        
        self.mode_elements['file'] = [self.button_getpath, self.label_import_path]
        
        self.place_by_mode('equation')
        
    def create_text_input(self, prompt, default):
        newlabel = tk.Label(self, text = prompt)
        newinput = tk.Entry(self, exportselection = 0)
        newinput.insert(0, default)
        return newlabel, newinput
    
    def update_from_sim(self, sim, mode):
        if (mode == 'equation'):
            self.entry_df.delete(0, tk.END)
            self.entry_df.insert(0, sim.driving_function)
        
    def switch(self, mode):
        for k in self.mode_elements.keys():
            if k != mode:
                for i in self.mode_elements[k]:
                    i.grid_forget()
        self.place_by_mode(mode)
    
    def place_by_mode(self, mode):
        if (mode == 'equation'):
            to_place = [[0, self.label_entry_df, self.entry_df], 
                        [1, self.label_entry_time, self.entry_time], 
                        [2, self.label_entry_samples, self.entry_samples]]
            for r in to_place:
                r[1].grid( row = r[0], column = 0, padx = 10, pady = 10 )
                r[2].grid( row = r[0], column = 1 )     
        if (mode == 'file'):
            self.button_getpath.grid( row = 0, column = 0, ipadx = 20, padx = 10, pady = 10 )
            self.label_import_path.grid( row = 0, column = 1, columnspan = 2 )
            self.label_entry_time.grid( row = 1, column = 0, padx = 10, pady = 10 )
            self.entry_time.grid( row = 1, column = 1 )   
            
    def pick_import_path(self):
        self.import_path = filedialog.askopenfilename()
        self.label_import_path['text'] = self.import_path
        self.input_file = lwio.ImportFile(self.import_path)
        
    def get_df(self):
        return self.entry_df.get()
    
    def get_time_bound(self):
        return int(self.entry_time.get())
    
    def get_samples(self):
        return int(self.entry_samples.get())
    
    def create_sim(self):
        return self.input_file.create_sim(self.get_time_bound())
