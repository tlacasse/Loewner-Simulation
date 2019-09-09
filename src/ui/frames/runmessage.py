from ui.frames.blank import BlankFrame
import tkinter as tk

class RunMessageFrame(BlankFrame):
    
    def __init__(self, master=None, control=None):
        super().__init__(master, control)
        
    def setup(self):
        self.label = tk.Label(self)
        self.label.grid(row=0, column=0, padx=75)
        
    def update(self, text):
        text = text + (' ' * 50)
        text = text[:50]
        self.label['text'] = text
