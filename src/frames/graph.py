import tkinter as tk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
        FigureCanvasTkAgg, NavigationToolbar2Tk)

class GraphFrame(tk.Frame):
    
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.setup()
        
    def setup(self):
        self.figure = Figure( figsize = (5, 4), dpi = 110 )
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
