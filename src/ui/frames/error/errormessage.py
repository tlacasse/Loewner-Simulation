from ui.frames.blank import BlankFrame
import tkinter as tk

class ErrorMessageFrame(BlankFrame):
    
    def __init__(self, master=None, control=None, message=''):
        super().__init__(master, control)
        self.message = message
        self.setup()
        
    def setup(self):
        self.label = tk.Label(self)
        self.label.grid(row=0, column=0, padx=50, pady=30)
        self.label['text'] = self.message
