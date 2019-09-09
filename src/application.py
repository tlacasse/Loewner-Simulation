import tkinter as tk
import tkinter.font as tkfont

from ui.container import MainAppFrameContainer
from control import Control

class Application(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.init_setup()
        
        self.control = Control(self)
        self.container = MainAppFrameContainer()
        self.container.setup(self, self.control)
        
    def init_setup(self):
        self.master.title('Loewner Simulation')
        self.master.geometry("1160x700")
        
        default_font = tkfont.nametofont("TkFixedFont")
        default_font.configure(size=10)
        self.master.option_add("*Font", default_font)

    def setup(self):
        pass # needed in container
        
    def __call__(self, key):
        return self.container(key)
