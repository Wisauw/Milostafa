from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=20)   

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    fotografia = models.ImageField(upload_to='productos')  

    def __str__(self):
        return str(self.fotografia)
