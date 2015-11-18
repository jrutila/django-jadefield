from pyjade.utils import process

class JadeTemplate(object):
    template = ""
    
    @property
    def as_html(self):
        return process(self.template)