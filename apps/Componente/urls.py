from django.urls import path, include

from django.contrib.auth import views as auth_views

from . import views
from django.contrib.auth.views import login_required
from .views import BuscarComponentesView, SearchResultsView



urlpatterns = [
    path('listar_componente/', login_required(views.ProductoList.as_view()), name="listar_componente"),
    path('agregar_componente/', login_required(views.ProductoCreate.as_view()), name="agregar_componente"),
    path('editar_componente/<int:pk>', login_required(views.ProductoUpdate.as_view()), name="editar_componente"),
    path('borrar_componente/<int:pk>', login_required(views.ProductoDelete.as_view()), name="borrar_componente"),

# Filtro
# nombre de componentes
    path('buscar_componentes/', BuscarComponentesView.as_view(), name="buscar_componentes"),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    
    # api
    path('productos/',  views.producto_collection , name='producto_collection'),
    path('productos/<int:pk>/', views.producto_element ,name='producto_element')
]