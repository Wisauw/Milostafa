"""Milostafa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView,LogoutView,TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', include('apps.Registro.urls')),
    path('usuario/', include('apps.Usuario.urls')),
    path('componente/', include('apps.Componente.urls')),
    # path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('faq', TemplateView.as_view(template_name='faq.html'), name='faq'),
    path('ofertas', TemplateView.as_view(template_name='ofertas.html'), name='ofertas'),

    #login
    path('accounts/login/', LoginView.as_view(redirect_authenticated_user=True,template_name='Usuario/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='Usuario/logout.html'), name='logout'),
    #Social login
    path('', include('social_django.urls', namespace='social')),

    #passwd
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="Usuario/password_reset.html"), name='password_reset'),
    path('reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="Usuario/password_reset_sent.html"), name='password_reset_done'),

    #uidb64: The user’s id encoded in base 64.
    #token: Token to check that the password is valid.
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="Usuario/password_reset_form.html"), name='password_reset_confirm'),
    path('reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="Usuario/password_reset_done.html"), name='password_reset_complete'),
   
    #Pwa
    path('', include('pwa.urls')),
]

urlpatterns += staticfiles_urlpatterns()