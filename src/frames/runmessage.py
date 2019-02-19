import tkinter as tk

class RunMessageFrame(tk.Frame):
    
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.setup() 
        
    def setup(self):
        self.label_time = tk.Label(self)
        self.label_time.grid( row = 0, column = 0, padx = 75 )
        
    def update(self, text):
        text = text + (' ' * 100)
        text = text[:50]
        self.label_time['text'] = text
