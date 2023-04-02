from django.test import TestCase
from apps.Registro.models import Cargo
from apps.Registro.forms import CargosForm

class CarreraFormCase(TestCase):
        
    def test_valid_form(self):
        cargo = Cargo.objects.create(nombre='Bodeguera',sueldo=150000)
        data = {'nombre': cargo.nombre, 'sueldo': cargo.sueldo,}
        form = CargosForm(data=data)
        self.assertTrue(form.is_valid())
        
    def test_invalid_form(self):
        cargo = Cargo.objects.create(nombre='',sueldo=100000)
        data = {'nombre': cargo.nombre, 'sueldo': cargo.sueldo }
        form = CargosForm(data=data)
        self.assertFalse(form.is_valid())
