from django.urls import path, include
from . import views
from django.contrib.auth.views import login_required
from .views import SearchResultsView, BuscarCargoView


urlpatterns = [

    # listar los cargos 
    path('listar_cargos/', login_required(views.CargoList.as_view()), name="listar_cargos"),    
    # agregar un cargo    
    path('agregar_cargo/', login_required(views.CargoCreate.as_view()), name="agregar_cargo"),
    # editar un cargo
    path('editar_cargo/<int:pk>', login_required(views.CargoUpdate.as_view()), name="editar_cargo"),
    # borrar un cargo
    path('borrar_cargo/<int:pk>', login_required(views.CargoDelete.as_view()), name="borrar_cargo"),

    # buscar un cargo
    path('buscar_cargo/', BuscarCargoView.as_view(), name="buscar_cargo"),
    path('search/', SearchResultsView.as_view(), name='search_results_cargo'),

    
]
