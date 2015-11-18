# django_jadefield

A django library for making a django field for inputting jade templates

## Basic usage

Use it like any regular model field:
```python
from jade_field.modelfields import JadeField

class MyModel(models.Model):
    name = models.CharField(max_length=255)
    template = JadeField()
```