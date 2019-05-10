import tkinter as tk
import tkinter.font as tkfont

from frames.input import InputFrame
from frames.runbutton import RunButtonFrame
from frames.graph import GraphFrame
from frames.runmessage import RunMessageFrame
from frames.exportbutton import ExportButtonFrame
from frames.mode_switch import ModeSwitchFrame
from frames.popups.export import create_export_popup

from control import AppControl
from loewner import LESimulation
import lwio

class Application(tk.Frame):
    
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.setup()
        self.control = AppControl(self)

    def setup(self):
        self.master.title('Loewner Simulation')
        self.master.geometry("1160x700")
        
        default_font = tkfont.nametofont("TkFixedFont")
        default_font.configure(size = 10)
        self.master.option_add("*Font", default_font)
        
        self.half_top = TopHalf(self)
        # self.half_bot = BotHalf(self)
        
        self.half_top.grid( row = 0, column = 0)
        #self.half_bot.grid( row = 1, column = 0)
        
#        

        
#        self.frame_runmessage.update('')
        
class TopHalf(tk.Frame):
    
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.setup()
        
    def setup(self):                   
        self.frame_inputs = InputFrame(self)
        self.frame_inputs.grid( row = 0, column = 1 )
        
        #self.frame_runbutton = RunButtonFrame(self, self.run_simulation)
        #self.frame_runbutton.grid( row = 1, column = 0 )
        
        #self.frame_runmessage = RunMessageFrame(self)
        #self.frame_runmessage.grid( row = 0, column = 2 )
        
        self.frame_modeswitch = ModeSwitchFrame(self, None) #self.switch_mode
        self.frame_modeswitch.grid( row = 0, column = 0 )     
    
class BotHalf(tk.Frame):
    
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.setup()
        
    def setup(self):
        self.master.frame_graphs_df = GraphFrame(self)
        self.master.frame_graphs_df.grid( row = 0, column = 0 )
        
        self.master.frame_graphs_hull = GraphFrame(self)
        self.master.frame_graphs_hull.grid( row = 0, column = 1 )  
        
        self.frame_exportbutton = ExportButtonFrame(self, self.show_export_popup)
        self.frame_exportbutton.grid( row = 3, column = 0, columnspan = 2 )
