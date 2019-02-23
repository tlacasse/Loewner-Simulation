import tkinter as tk

class ExportButtonFrame(tk.Frame):
    
    def __init__(self, master = None, export_func = None):
        super().__init__(master)
        self.master = master
        self.setup(export_func) 
        
    def setup(self, export_func):
        self.button_run = tk.Button(self)
        self.button_run['text'] = 'Export (csv)'
        self.button_run['command'] = export_func
        self.button_run.grid( row = 0, column = 0, ipadx = 20 )
