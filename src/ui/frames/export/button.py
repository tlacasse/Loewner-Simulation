from ui.frames.blank import BlankFrame
import tkinter as tk

class ButtonFrame(BlankFrame):
    
    def __init__(self, master=None, control=None):
        super().__init__(master, control)
        
    def setup(self):
        button_run = tk.Button(self)
        button_run['text'] = 'Export'
        button_run['command'] = self.control.export_simulation
        button_run.grid(row=0, column=0, ipadx=20)
