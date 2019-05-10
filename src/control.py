from loewner import LESimulation
import lwio
import time

class AppControl:
    
    def __init__(self, app):
        self.app = app
        self.sim = None
        
#    def execute(self, func):
#        try:
#            start = time.time()
#            func()
#            stop = time.time()
#            self.frame_runmessage.update('Computation Time: ' + str(stop - start) + 's')
#        except Exception as e:
#            message = str(e)
#            #message = message[(message.rfind(')')+1):]
#            self.frame_runmessage.update(message) #todo: improve this 
    
#    def show_export_popup(self):
#        if (self.sim != None):
#            self.frame_export = create_export_popup(self.export_simulation)
#            
#    def switch_mode(self):
#        self.frame_inputs.switch(self.frame_modeswitch.get_mode())
#
#    def run_simulation(self):
#        self.execute(self.__run_simulation)
#        
#    def export_simulation(self):
#        self.execute(self.__export_simulation)
#            
#    def __run_simulation(self):
#        if (self.frame_modeswitch.get_mode() == 'equation'):
#            sim = LESimulation()
#            sim.init_equation(self.frame_inputs.get_df(), 
#                                   self.frame_inputs.get_time_bound(), 
#                                   self.frame_inputs.get_samples())
#        if (self.frame_modeswitch.get_mode() == 'file'):
#            sim = self.frame_inputs.create_sim()
#
#        self.sim = sim
#        self.frame_inputs.update_from_sim(sim, self.frame_modeswitch.get_mode())
#        
#        sim.compute_hull()
#        
#        self.frame_graphs_df.update(sim.time_domain, sim.samples)
#        self.frame_graphs_hull.update(sim.hull.real, sim.hull.imag)
#            
#    def __export_simulation(self):
#        what = self.frame_export.get_what_to_export()
#        export_samples = False
#        export_hull = False
#        if (what == 'samples' or what == 'both'):
#            export_samples = True
#        if (what == 'hull' or what == 'both'):
#            export_hull = True
#        path = self.frame_export.export_path
#        lwio.export_sim(self.sim, path, export_samples, export_hull)
    