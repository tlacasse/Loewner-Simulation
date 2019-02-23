import tkinter as tk
import tkinter.font as tkfont

from frames.input import InputFrame
from frames.runbutton import RunButtonFrame
from frames.graph import GraphFrame
from frames.runmessage import RunMessageFrame
from frames.exportbutton import ExportButtonFrame

from loewner import LESimulation
import lwio
import time

class Application(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.setup()
        self.sim = None

    def setup(self):
        self.master.title('Loewner Simulation')
        self.master.geometry("1160x700")
        
        default_font = tkfont.nametofont("TkFixedFont")
        default_font.configure(size=10)
        self.master.option_add("*Font", default_font)
        
        self.frame_inputs = InputFrame(self)
        self.frame_inputs.grid( row = 0, column = 0 )
        
        self.frame_runbutton = RunButtonFrame(self, self.run_simulation)
        self.frame_runbutton.grid( row = 1, column = 0 )
        
        self.frame_runmessage = RunMessageFrame(self)
        self.frame_runmessage.grid( row = 0, column = 2 )
        
        self.frame_graphs_df = GraphFrame(self)
        self.frame_graphs_df.grid( row = 2, column = 0, columnspan = 2 )
        
        self.frame_graphs_hull = GraphFrame(self)
        self.frame_graphs_hull.grid( row = 2, column = 2, columnspan = 2 )
        
        self.frame_exportbutton = ExportButtonFrame(self, self.export_simulation)
        self.frame_exportbutton.grid( row = 3, column = 0, columnspan = 2 )
        
        self.frame_runmessage.update('')
        
    def execute(self, func):
        try:
            start = time.time()
            func()
            stop = time.time()
            self.frame_runmessage.update('Computation Time: ' + str(stop - start) + 's')
        except Exception as e:
            message = str(e)
            message = message[(message.rfind(')')+1):]
            self.frame_runmessage.update(message) #todo: improve this

    def run_simulation(self):
        self.execute(self.__run_simulation)
        
    def export_simulation(self):
        self.execute(self.__export_simulation)
            
    def __run_simulation(self):
        sim = LESimulation(self.frame_inputs.get_df(), 
                               self.frame_inputs.get_time_bound(), 
                               self.frame_inputs.get_samples())

        self.sim = sim
        self.frame_inputs.update_from_sim(sim)
        
        sim.compute_hull()
        
        self.frame_graphs_df.update(sim.time_domain, sim.samples)
        self.frame_graphs_hull.update(sim.hull.real, sim.hull.imag)
            
    def __export_simulation(self):
        if (self.sim != None):
            lwio.export_sim(self.sim, 'sim.csv', True, True)
