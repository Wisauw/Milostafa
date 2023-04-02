from django import forms
from .models import Cargo, Trabajador

class CargosForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['nombre', 'sueldo']

        labels = {
            'nombre': 'Nombre',            
            'sueldo': 'sueldo Pesos Chilenos',

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),            
            'sueldo': forms.TextInput(attrs={'class': 'form-control'}),           
        }
