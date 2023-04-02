from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria
from .forms import ProductosForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q 
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductoSerializer
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 


# Create your views here.
class ProductoCreate(CreateView):
    model = Producto
    form_class = ProductosForm
    template_name = 'Componente/agregar_componente.html'
    success_url = reverse_lazy("listar_componente")

class ProductoList(ListView):
    model = Producto
    template_name = 'Componente/listar_componente.html'
    
class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductosForm
    template_name = 'Componente/editar_componente.html'
    success_url = reverse_lazy('listar_componente')

        

class ProductoDelete(DeleteView):
    model = Producto
    template_name = 'Componente/borrar_componente.html'
    success_url = reverse_lazy('listar_componente')

class BuscarComponentesView(ListView):
    model = Producto
    template_name = 'Componente/buscar_componentes.html'

class SearchResultsView(ListView):
    model = Producto
    template_name = 'Componente/search_results.html'
    
    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Producto.objects.filter(
            Q(nombre__icontains=query) )
        
        return object_list
    
#API
# El decorador @api_view verifica que la solicitud HTTP apropiada 
@api_view(['GET', 'POST'])
def producto_collection(request):
    if request.method == 'GET':
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Si el proceso de deserialización funciona, devolvemos una respuesta con un código 201 (creado)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # si falla el proceso de deserialización, devolvemos una respuesta 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def producto_element(request, pk):
    producto = get_object_or_404(Producto, id=pk)

    if request.method == 'GET':
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT': 
        producto_new = JSONParser().parse(request) 
        serializer = ProductoSerializer(producto, data=producto_new) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)