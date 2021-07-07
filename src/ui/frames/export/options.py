from ui.frames.blank import BlankFrame
import tkinter as tk

class OptionsFrame(BlankFrame):
    
    def __init__(self, master=None, control=None):
        super().__init__(master, control)
        
    def setup(self):
        self.check_samples = tk.IntVar(value=1)
        self.check_hull = tk.IntVar(value=1)
        self.check_xy = tk.IntVar()
        self.box_samples = self.setup_box('Samples', 0, self.check_samples)
        self.box_hull = self.setup_box('Hull', 1, self.check_hull)
        self.box_xy = self.setup_box('Hull X & Y', 2, self.check_xy)
    
    def setup_box(self, value, num, var):
        def pad_box_prompt(prompt):
            max_len = 10
            return (prompt + (' ' * 20))[:max_len]
        
        check = tk.Checkbutton(self, text=pad_box_prompt(value), 
                               variable=var, padx=10)
        check.grid(row=0, column=num)
        return check
    
    def get_what_to_export(self):
        return {
            'samples': bool(self.check_samples.get()),
            'hull': bool(self.check_hull.get()), 
            'xy': bool(self.check_xy.get())
        }
