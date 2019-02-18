import tkinter as tk
import tkinter.font as tkfont
import time

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
        FigureCanvasTkAgg, NavigationToolbar2Tk)

from loewner import LESimulation

class Application(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.setup()

    def setup(self):
        self.master.title('Loewner Simulation')
        self.master.geometry("1160x700")
        
        default_font = tkfont.nametofont("TkFixedFont")
        default_font.configure(size=10)
        self.master.option_add("*Font", default_font)
        
        self.frame_inputs = InputFrame(self)
        self.frame_inputs.grid( row = 0, column = 0 )
        
        self.frame_runbutton = ButtonFrame(self)
        self.frame_runbutton.grid( row = 1, column = 0 )
        
        self.frame_runmessage = RunMessageFrame(self)
        self.frame_runmessage.grid( row = 0, column = 2 )
        
        self.frame_graphs_df = GraphFrame(self)
        self.frame_graphs_df.grid( row = 2, column = 0, columnspan = 2 )
        
        self.frame_graphs_hull = GraphFrame(self)
        self.frame_graphs_hull.grid( row = 2, column = 2, columnspan = 2 )
        
        self.frame_runmessage.update('')

    def run_simulation(self):
        sim = LESimulation(self.frame_inputs.entry_df.get(), 
                           int(self.frame_inputs.entry_time.get()), 
                           int(self.frame_inputs.entry_samples.get()))
        self.frame_inputs.update(sim)
        
        start = time.time()
        sim.compute_hull()
        stop = time.time()
        
        self.frame_runmessage.update('Computation Time: ' + str(stop - start) + 's')
        self.frame_graphs_df.update(sim.time_domain, sim.samples)
        self.frame_graphs_hull.update(sim.hull.real, sim.hull.imag)
        
class InputFrame(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.setup() 
        
    def setup(self):
        self.label_entry_df, self.entry_df = (
            self.create_text_input('Driving Function (t):', 't', 0))
        self.label_entry_time, self.entry_time = (
            self.create_text_input('Time Bound:', '20', 1))
        self.label_entry_samples, self.entry_samples = (
            self.create_text_input('# Samples:', '1000', 2))
        
    def create_text_input(self, prompt, default, i):
        newlabel = tk.Label(self, text = prompt)
        newinput = tk.Entry(self, exportselection = 0)
        newinput.insert(0, default)
        
        newlabel.grid( row = i, column = 0, padx = 10, pady = 10 )
        newinput.grid( row = i, column = 1 )
        
        return newlabel, newinput
    
    def update(self, sim):
        self.entry_df.delete(0, tk.END)
        self.entry_df.insert(0, sim.driving_function_text)
    
class ButtonFrame(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.setup() 
        
    def setup(self):
        self.button_run = tk.Button(self)
        self.button_run['text'] = 'Run'
        self.button_run['command'] = self.master.run_simulation
        self.button_run.grid( row = 0, column = 0, ipadx = 20 )
        
class RunMessageFrame(tk.Frame):
    
    def __init__(self, master=None):
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
        
class GraphFrame(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.setup()
        
    def setup(self):
        self.figure = Figure(figsize=(5, 4), dpi = 110)
        self.canvas = FigureCanvasTkAgg(self.figure, master = self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack( side = tk.TOP, fill = tk.BOTH,
                                    padx = 10, pady = 10 )
        self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        self.toolbar.update()
        self.toolbar.pack( side = tk.BOTTOM )
        
    def update(self, x, y):
        self.figure.clf()
        self.figure.add_subplot(111).plot(x, y)
        self.canvas.draw()
