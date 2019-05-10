import tkinter as tk
import tkinter.filedialog as filedialog

def create_export_popup(export_func):
    popup = tk.Toplevel()
    popup.wm_title('Export Simulation')
    
    frame = ExportFrame(popup, export_func)
    frame.grid( row = 0, column = 0 )
    
    return frame

class ExportFrame(tk.Frame):
    
    def __init__(self, master = None, export_func = None):
        super().__init__(master)
        self.master = master
        self.export_func = export_func
        self.export_path = ''
        self.grid()
        self.setup()
        
    def setup(self):
        self.button_getpath = tk.Button(self)
        self.button_getpath['text'] = 'Choose Export Path'
        self.button_getpath['command'] = self.pick_export_path
        self.button_getpath.grid( row = 0, column = 0, ipadx = 20 )
        
        self.label_export_path = tk.Label(self, text = '')
        self.label_export_path.grid( row = 0, column = 1, columnspan = 3 )
        
        self.check_samples = tk.IntVar(value=1)
        self.check_hull = tk.IntVar(value=1)
        self.check_xy = tk.IntVar()
        
        self.box_exportwhat_samples = self.setup_box('Samples', 0, self.check_samples)
        self.box_exportwhat_hull = self.setup_box('Hull', 1, self.check_hull)
        self.box_exportwhat_xy = self.setup_box('Hull X & Y', 2, self.check_xy)
        
        self.button_run = tk.Button(self)
        self.button_run['text'] = 'Export'
        self.button_run['command'] = self.run_and_close
        self.button_run.grid( row = 2, column = 1, ipadx = 20 )
        
    def setup_box(self, value, num, var):
        check = tk.Checkbutton(self, text=self._pad_box_prompt(value), 
                               variable=var, padx = 10)
        check.grid( row = 1, column = num )
        return check
    
    def _pad_box_prompt(self, prompt):
        max_len = 10
        return (prompt + (' ' * 20))[:max_len]

    def run_and_close(self):
        self.export_func()
        self.master.destroy()
        
    def pick_export_path(self):
        self.export_path = filedialog.asksaveasfilename()
        self.label_export_path['text'] = self.export_path
        self.master.lift()
        self.master.focus_force()
        
    def get_what_to_export(self):
        return {
            'samples': bool(self.check_samples.get()),
            'hull': bool(self.check_hull.get()), 
            'xy': bool(self.check_xy.get())
        }
