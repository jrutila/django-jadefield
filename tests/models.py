from django.db import models
from jade_field.modelfields import JadeField

class JadeModel(models.Model):
    #class Meta:
        #app_label = "tests"
    name = models.CharField(max_length=10)
    template = JadeField()