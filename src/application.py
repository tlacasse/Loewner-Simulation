import tkinter as tk
import tkinter.font as tkfont

from ui.container import FrameContainer
from control import Control

class Application(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.control = Control(self)
        self.frames = []
        self.container = FrameContainer()
        self.container.setup(self, self.control)

    def setup(self):
        self.master.title('Loewner Simulation')
        self.master.geometry("1160x700")
        
        default_font = tkfont.nametofont("TkFixedFont")
        default_font.configure(size=10)
        self.master.option_add("*Font", default_font)
        
    def __call__(self, key):
        matches = [f for f in self.frames if f.id == key]
        if (matches):
            return matches[0]
        else:
            return None
