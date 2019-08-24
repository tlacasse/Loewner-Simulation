import xml.etree.ElementTree as et

from ui.frames.blank import BlankFrame
from ui.frames.input import InputFrame
from ui.frames.graph import GraphFrame
from ui.frames.runbutton import RunButtonFrame
from ui.frames.runmessage import RunMessageFrame

class FrameContainer:
    
    def __init__(self, config_xml_file='frames.xml'):
        self.config = et.parse(config_xml_file).getroot()
        self.map = {}
        self.map['blank'] = (lambda m, c: BlankFrame(m, c))
        self.map['input'] = (lambda m, c: InputFrame(m, c))
        self.map['graph'] = (lambda m, c: GraphFrame(m, c))
        self.map['runbutton'] = (lambda m, c: RunButtonFrame(m, c))
        self.map['runmessage'] = (lambda m, c: RunMessageFrame(m, c))
        
    def setup(self, app, control_obj):
        self._setup(app, self.config, control_obj, app)
    
    def _setup(self, master, node, control_obj, app):
        master.grid()
        for child in node:
            frame = self.map[child.tag](master, control_obj)
            frame.grid(row=child.get('row'), column=child.get('col'))
            frame.id = child.get('id')
            app.frames.append(frame)
            self._setup(frame, child, control_obj, app)
        master.setup()
