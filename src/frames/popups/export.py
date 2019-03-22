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
        self.var_exportwhat = tk.StringVar()
        
        self.button_getpath = tk.Button(self)
        self.button_getpath['text'] = 'Choose Export Path'
        self.button_getpath['command'] = self.pick_export_path
        self.button_getpath.grid( row = 0, column = 0, ipadx = 20 )
        
        self.label_export_path = tk.Label(self, text = 'TEST')
        self.label_export_path.grid( row = 0, column = 1, columnspan = 2 )
        
        self.radio_exportwhat_samples = self.setup_radio('Samples', 0)
        self.radio_exportwhat_hull = self.setup_radio('Hull', 1)
        self.radio_exportwhat_both = self.setup_radio('Both', 2)
        
        self.radio_exportwhat_both.select()
        
        self.button_run = tk.Button(self)
        self.button_run['text'] = 'Export'
        self.button_run['command'] = self.run_and_close
        self.button_run.grid( row = 2, column = 1, ipadx = 20 )
        
    def setup_radio(self, value, num):
        radio = tk.Radiobutton(self, text=value,
                        variable=self.var_exportwhat, value=value.lower())
        radio.grid( row = 1, column = num)
        return radio

    def run_and_close(self):
        self.export_func()
        self.master.destroy()
        
    def pick_export_path(self):
        self.export_path = filedialog.asksaveasfilename()
        self.label_export_path['text'] = self.export_path
        self.master.lift()
        self.master.focus_force()
        
    def get_what_to_export(self):
        return self.var_exportwhat.get()
