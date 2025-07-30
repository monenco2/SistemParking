from django.contrib import admin
from django.urls import path, include

from apps.usuarios import*
from django.contrib.auth import views as auth_views
from apps.facturacion import*
from apps.horaparqueo import*
from apps.pagofinal import*
from apps.rol import*
from apps.servicio import*
from apps.vehiculo import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.api.routers')),
    path('usua/',auth_views.LoginView.as_view(template_name='registration/usua.html')),
    path('factu/',auth_views.LoginView.as_view(template_name='registration/factu.html')),
    path('hpar/',auth_views.LoginView.as_view(template_name='registration/hpar.html')),
    path('pg/',auth_views.LoginView.as_view(template_name='registration/pg.html')),
    path('rl/',auth_views.LoginView.as_view(template_name='registration/rl.html')),
    path('servi/',auth_views.LoginView.as_view(template_name='registration/servi.html')),
    path('vehi/',auth_views.LoginView.as_view(template_name='registration/vehi.html')),
]
