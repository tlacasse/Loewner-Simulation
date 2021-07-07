from ui.frames.blank import BlankFrame
import tkinter as tk
import tkinter.filedialog as filedialog

class PathFrame(BlankFrame):
    
    def __init__(self, master=None, control=None):
        super().__init__(master, control)
        self.export_path = None
        
    def setup(self):
        button = tk.Button(self)
        button['text'] = 'Choose Export Path'
        button['command'] = self.pick_export_path
        button.grid(row=0, column=0, ipadx=20)
        
        self.label = tk.Label(self, text='')
        self.label.grid(row=0, column=1)
        
    def pick_export_path(self):
        self.export_path = filedialog.asksaveasfilename()
        self.label['text'] = self.export_path
        self.master.master.lift()
        self.master.master.focus_force()
        
    def get_export_path(self):
        return self.export_path
