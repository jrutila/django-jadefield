from django.db import models
from django.utils.translation import ugettext_lazy as _
from jade_field.jade_template import JadeTemplate

class JadeField(models.TextField):
    description = _("Jade template")
    
    def __init__(self, *args, **kwargs):
        super(JadeField, self).__init__(*args, **kwargs)
        
    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return None
        val = JadeTemplate()
        val.template = value
        return val
        
    def to_python(self, value):
        if isinstance(value, JadeTemplate):
            return value
        if value is None:
            return None
        val = JadeTemplate()
        val.template = value
        return val
