import tkinter as tk

class RunButtonFrame(tk.Frame):
    
    def __init__(self, master = None, run_func = None):
        super().__init__(master)
        self.master = master
        self.setup(run_func) 
        
    def setup(self, run_func):
        self.button_run = tk.Button(self)
        self.button_run['text'] = 'Run'
        self.button_run['command'] = run_func
        self.button_run.grid( row = 0, column = 0, ipadx = 20 )
