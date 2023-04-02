from django.test import TestCase
from django.template.defaultfilters import slugify
from apps.Registro.models import Cargo

class CarreraTestCase(TestCase):
    def setUp(self):
        Cargo.objects.create(nombre="CARGO1",sueldo=120000)
        Cargo.objects.create(nombre="CARGO2",sueldo=130000)

    def test_ingresar_carreras(self):
        """Los cargos se registran correctamente en la BD"""
        cargo_1 = Cargo.objects.get(nombre="CARGO1")
        cargo_2 = Cargo.objects.get(nombre="CARGO2")
        self.assertEqual(cargo_1.sueldo, 120000)
        self.assertEqual(cargo_2.sueldo, 130000)
