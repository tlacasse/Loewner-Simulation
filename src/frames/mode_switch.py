import tkinter as tk

class ModeSwitchFrame(tk.Frame):
    
    def __init__(self, master = None, onclick = None):
        super().__init__(master)
        self.master = master
        self.setup(onclick) 
        
    def setup(self, onclick):
        self.var_mode = tk.StringVar()
        
        self.radio_mode_equation = tk.Radiobutton(self, text = 'Equation',
                        variable = self.var_mode, value='equation')
        
        self.radio_mode_file = tk.Radiobutton(self, text = 'File',
                        variable = self.var_mode, value='file')
        
        self.radio_mode_equation.select()
        
        self.radio_mode_equation['command'] = onclick
        self.radio_mode_file['command'] = onclick
        
        self.radio_mode_equation.grid( row = 0, column = 0 )
        self.radio_mode_file.grid( row = 0, column = 1 )
        
    def get_mode(self):
        return self.var_mode.get()
