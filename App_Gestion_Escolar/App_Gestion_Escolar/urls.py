"""
URLs principal — App_Gestion_Escolar (Parte III).

PASO 2 DEL PDF (Parte III): Instalando la Aduana Principal.
Importamos las vistas de autenticación nativas de Django
y creamos las rutas /login/ y /logout/.
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),

    # Redirección: cuando alguien entra a "/" lo manda al login automáticamente
    path('', lambda request: redirect('login'), name='inicio'),

    # Autenticación
    path('login/',  auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Pabellones del liceo
    path('alumnos/',    include('alumnos.urls')),
    path('profesores/', include('profesores.urls')),
    path('cursos/',     include('cursos.urls')),
]
