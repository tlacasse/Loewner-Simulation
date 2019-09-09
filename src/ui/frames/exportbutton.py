from ui.frames.blank import BlankFrame
import tkinter as tk

class ExportButtonFrame(BlankFrame):
    
    def __init__(self, master=None, control=None):
        super().__init__(master, control)
        
    def setup(self):
        button_run = tk.Button(self)
        button_run['text'] = 'Export (csv)'
        button_run['command'] = self.control.display_export_popup
        button_run.grid(row=0, column=0, ipadx=20)
