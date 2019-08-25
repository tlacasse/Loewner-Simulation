from ui.frames.blank import BlankFrame
import tkinter as tk

class RunButtonFrame(BlankFrame):
    
    def __init__(self, master=None, control=None):
        super().__init__(master, control)
        
    def setup(self):
        def command():
            self.control.execute(self.control.run_simulation)
        
        button_run = tk.Button(self)
        button_run['text'] = 'Run'
        button_run['command'] = command
        button_run.grid(row=0, column=0, ipadx=20)
