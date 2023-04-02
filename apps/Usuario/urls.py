from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import RegistroUsuario, UserList
from django.contrib.auth.views import LoginView,LogoutView,TemplateView

from django.contrib.auth.views import login_required


urlpatterns = [
    path('registrar', RegistroUsuario.as_view(), name="registrar"),
    path('listar', login_required(UserList.as_view()), name="list_user"),
    # path('accounts/login/', LoginView.as_view(redirect_authenticated_user=True,template_name='Usuario/login.html'), name='login'),
    # path('logout/', LogoutView.as_view(template_name='Usuario/logout.html'), name='logout'),

    

]
