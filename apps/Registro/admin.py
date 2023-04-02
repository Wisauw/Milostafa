from django.contrib import admin
from .models import Trabajador, Cargo

# Register your models here.
admin.site.register(Cargo)
admin.site.register(Trabajador)
