from django.urls import path
from . import views

app_name = 'profesores'

urlpatterns = [
    path('',       views.lista_profesores, name='lista'),
    path('crear/', views.crear_profesor,   name='crear'),
]
