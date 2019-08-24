import time

class Control:
    
    def __init__(self, app):
        self.app = app

    def execute(self, func):
        try:
            start = time.time()
            func()
            stop = time.time()
            self.frame_runmessage.update('Computation Time: ' + str(stop - start) + 's')
        except Exception:
            pass
