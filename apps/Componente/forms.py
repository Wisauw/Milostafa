from django import forms
from .models import Producto, Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

        labels = {
            'nombre': 'Nombre',            

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),            
                    
        }

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['categoria','codigo','nombre','marca','precio','stock','fotografia']

        labels = {
            'categoria':'Categoria',
            'codigo': 'Codigo', 
            'nombre': 'Nombre', 
            'marca': 'Marca', 
            'precio': 'Precio', 
            'stock': 'Stock',
            'fotografia': 'Fotografia'
            


        }
        widgets = {
            'categoria':forms.Select(choices="Categorias", attrs={'class':'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}), 
            'marca': forms.TextInput(attrs={'class': 'form-control'}), 
            'precio': forms.TextInput(attrs={'class': 'form-control'}), 
            'stock': forms.TextInput(attrs={'class': 'form-control'}),
            'fotografia':forms.FileInput(attrs={'class':'formcontrol','type':'file'})
            
        }