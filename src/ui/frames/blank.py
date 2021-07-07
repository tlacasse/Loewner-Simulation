import tkinter as tk

class BlankFrame(tk.Frame):
    
    def __init__(self, master=None, control=None):
        super().__init__(master)
        self.master = master
        self.control = control
        self.id = None
        
    def setup(self):
        pass
