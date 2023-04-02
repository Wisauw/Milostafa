from django.shortcuts import render, redirect
from .models import Cargo, Trabajador
from .forms import CargosForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.db.models import Q 
# Create your views here.

# def listar_cargos(request):
#     cargos = Cargo.objects.all()
#     return render(request, "Registro/listar_cargos.html", {'cargos': cargos})

# def agregar_cargo(request):
#     if request.method == "POST":
#         form = CargosForm(request.POST)
#         if form.is_valid():
#             model_instance = form.save(commit=False)
#             model_instance.save()
#             return redirect("agregar_cargo")
#     else:
#         form = CargosForm()
#         return render(request, "Registro/agregar_cargo.html", {'form': form})
    
# def borrar_cargo(request, cargo_id):
#     instancia = Cargo.objects.get(id=cargo_id)
#     instancia.delete()
#     return redirect('listar_cargos')

# def editar_cargo(request, cargo_id):
#     instancia = Cargo.objects.get(id=cargo_id)
#     form = CargosForm(instance=instancia)
#     if request.method == "POST":
#             # Actualizamos el formulario con los datos recibidos
#             form = CargosForm(request.POST, instance=instancia)
#             # Si el formulario es válido...
#             if form.is_valid():
#                 # Guardamos el formulario pero sin confirmarlo,
#                 # así conseguiremos una instancia para manipular antes de grabar
#                 instancia = form.save(commit=False)
#                 # Podemos guardar cuando queramos
#                 instancia.save()
    
                

#         # Si llegamos al final renderizamos el formulario
#     return render(request, "Registro/editar_cargo.html", {'form': form})

class CargoCreate(CreateView):
    model = Cargo
    form_class = CargosForm
    template_name = 'Registro/agregar_cargo.html'
    success_url = reverse_lazy("listar_cargos")

class CargoList(ListView):
    model = Cargo
    template_name = 'Registro/listar_cargos.html'
    
class CargoUpdate(UpdateView):
    model = Cargo
    form_class = CargosForm
    template_name = 'Registro/editar_cargo.html'
    success_url = reverse_lazy('listar_cargos')

        

class CargoDelete(DeleteView):
    model = Cargo
    template_name = 'Registro/borrar_cargo.html'
    success_url = reverse_lazy('listar_cargos')

#-------------- filtros----------------
class BuscarCargoView(ListView):
    model = Cargo
    template_name = 'Registro/buscar_cargo.html'

class SearchResultsView(ListView):
    model = Cargo
    template_name = 'Registro/search_results.html'
    
    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Cargo.objects.filter(
            Q(nombre__icontains=query) )
        
        return object_list