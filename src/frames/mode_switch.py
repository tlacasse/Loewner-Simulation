import tkinter as tk

class ModeSwitchFrame(tk.Frame):
    
    def __init__(self, master = None, onclick = None):
        super().__init__(master)
        self.master = master
        self.setup(onclick) 
        
    def setup(self, onclick):
        self['padx'] = 10
        
        self.labelframe = tk.LabelFrame(self, text = 'Input Method')
        self.labelframe.grid( row = 0, column = 0)
        base = self.labelframe
        
        self.var_mode = tk.StringVar()
        
        self.radio_equation = tk.Radiobutton(
                base, text = 'Equation', variable = self.var_mode, value ='equation')
        
        self.radio_file = tk.Radiobutton(base, text = 'File    ', 
                                         variable = self.var_mode, value='file')
        
        self.radio_equation.select()
        
        self.radio_equation['command'] = onclick
        self.radio_file['command'] = onclick
        
        self.radio_equation.grid( row = 1, column = 0 )
        self.radio_file.grid( row = 2, column = 0 )
        
    def get_mode(self):
        return self.var_mode.get()
