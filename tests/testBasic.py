from django.test import TestCase
from tests.models import JadeModel
import sure

class BasicTestCase(TestCase):
    def test_getting_html(self):
        JadeModel.objects.create(name="j1", template="h1 Hello World")
        j1 = JadeModel.objects.all()[0]
        j1.name.should.equal("j1")
        j1.template.template.should.equal("h1 Hello World")
        j1.template.as_html.should.equal("<h1>Hello World</h1>")