import xml.etree.ElementTree as et

from ui.frames.blank import BlankFrame
from ui.frames.input import InputFrame
from ui.frames.graph import GraphFrame
from ui.frames.runbutton import RunButtonFrame
from ui.frames.runmessage import RunMessageFrame
from ui.frames.exportbutton import ExportButtonFrame

from ui.frames.export.path import PathFrame
from ui.frames.export.options import OptionsFrame
from ui.frames.export.button import ButtonFrame

class FrameContainer:
    
    def __init__(self, config_xml_file):
        self.config = et.parse(config_xml_file).getroot()
        self.frames = []
        self.map = {}
        self.map['blank'] = (lambda m, c: BlankFrame(m, c))
        self.root = None
        
    def setup(self, root, control_obj):
        self.root = root
        self._setup(root, self.config, control_obj)
    
    def _setup(self, master, node, control_obj):
        master.grid()
        for child in node:
            frame = self.map[child.tag](master, control_obj)
            frame.grid(row=child.get('row'), column=child.get('col'))
            frame.id = child.get('id')
            self.frames.append(frame)
            self._setup(frame, child, control_obj)
        master.setup()
        
    def __call__(self, key):
        matches = [f for f in self.frames if f.id == key]
        if (matches):
            return matches[0]
        else:
            return None

class MainAppFrameContainer(FrameContainer):
    
    def __init__(self, config_xml_file='config/frames.xml'):
        super().__init__(config_xml_file)
        self.map['input'] = (lambda m, c: InputFrame(m, c))
        self.map['graph'] = (lambda m, c: GraphFrame(m, c))
        self.map['runbutton'] = (lambda m, c: RunButtonFrame(m, c))
        self.map['runmessage'] = (lambda m, c: RunMessageFrame(m, c))
        self.map['exportbutton'] = (lambda m, c: ExportButtonFrame(m, c))

class ExportPopupFrameContainer(FrameContainer):
    
    def __init__(self, config_xml_file='config/export.xml'):
        super().__init__(config_xml_file)
        self.map['path'] = (lambda m, c: PathFrame(m, c))
        self.map['options'] = (lambda m, c: OptionsFrame(m, c))
        self.map['button'] = (lambda m, c: ButtonFrame(m, c))
